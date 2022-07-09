from django.urls import path, include
from rest_framework import routers
from core.api import viewsets

app_name = 'core'

router = routers.DefaultRouter()
router.register(r'action-categories', viewsets.ActionCategoryViewSet)
router.register(r'action-details', viewsets.ActionDetailViewSet)
router.register(r'action-voices', viewsets.ActionVoiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
