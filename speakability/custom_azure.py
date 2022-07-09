from storages.backends.azure_storage import AzureStorage
from django.conf import settings

class AzureMediaStorage(AzureStorage):
    account_name = 'speakability'
    account_key = settings.AZURE_STORAGE_KEY
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'speakability'
    account_key = settings.AZURE_STORAGE_KEY
    azure_container = 'static'
    expiration_secs = None