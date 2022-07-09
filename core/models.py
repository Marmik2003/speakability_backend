from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class ActionCategory(BaseModel):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons/')

    def __str__(self):
        return self.name


class ActionDetail(BaseModel):
    class LanguageChoices(models.TextChoices):
        ENGLISH_MALE = 'en-IN-PrabhatNeural'
        ENGLISH_FEMALE = 'en-IN-NeerjaNeural'
        HINDI_MALE = 'hi-IN-MadhurNeural'
        HINDI_FEMALE = 'hi-IN-SwaraNeural'
        GUJARATI_MALE = 'gu-IN-NiranjanNeural'
        GUJARATI_FEMALE = 'gu-IN-DhwaniNeural'

    category = models.ForeignKey(ActionCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='action_image')
    language = models.CharField(
        max_length=40, 
        choices=LanguageChoices.choices, 
        default=LanguageChoices.ENGLISH_MALE
    )

    def __str__(self):
        return self.name


class ActionVoice(BaseModel):
    action = models.ForeignKey(ActionDetail, on_delete=models.CASCADE)
    voice = models.FileField(upload_to='action_voice')

    def __str__(self):
        return self.name
