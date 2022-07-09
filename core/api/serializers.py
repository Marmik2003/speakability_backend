from rest_framework import serializers
from core.models import ActionCategory, ActionDetail, ActionVoice


class ActionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionCategory
        fields = '__all__'


class ActionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionDetail
        fields = '__all__'


class ActionVoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionVoice
        fields = '__all__'
