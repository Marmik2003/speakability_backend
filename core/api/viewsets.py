import io

from django.conf import settings
from django.core.files.base import ContentFile
from rest_framework import mixins, viewsets, status, permissions
from rest_framework.response import Response
import azure.cognitiveservices.speech as speechsdk

from core.models import ActionCategory, ActionDetail, ActionVoice
from core.api.serializers import ActionCategorySerializer, ActionDetailSerializer, ActionVoiceSerializer


AZURE_SPEECH_KEY = settings.AZURE_SPEECH_KEY


class ActionCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ActionCategory.objects.all()
    serializer_class = ActionCategorySerializer

    def get_queryset(self):
        return ActionCategory.objects.all()


class ActionDetailViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = ActionDetail.objects.all()
    serializer_class = ActionDetailSerializer
    filterset_fields = ('category', 'language')

    def get_queryset(self):
        return ActionDetail.objects.all()

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    def _convert_to_speech(self, text, language):
        subscription_key = AZURE_SPEECH_KEY
        speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region='centralindia', speech_recognition_language=language)
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

        result = synthesizer.speak_text_async(text).get()
        file_bytes = io.BytesIO(result.audio_data)
        return ContentFile(file_bytes.getvalue(), name=f"{language}-{text}.wav")

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        language = serializer.validated_data['language']
        text = serializer.validated_data['text']
        self.perform_create(serializer)
        stream = self._convert_to_speech(text, language)
        voice = ActionVoice(action=serializer.instance, voice=stream)
        voice.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        language = serializer.validated_data['language']
        text = serializer.validated_data['text']
        self.perform_update(serializer)
        stream = self._convert_to_speech(text, language)
        voice = ActionVoice.objects.get(action=instance)
        voice.voice = stream
        voice.save()
        return Response(serializer.data)


class ActionVoiceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ActionVoice.objects.all()
    serializer_class = ActionVoiceSerializer

    def get_queryset(self):
        return ActionVoice.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        stream = instance.voice
        return Response(stream.read())
