from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimezoneEntryViewSet

router = DefaultRouter()
router.register('', TimezoneEntryViewSet, basename='timezones')

urlpatterns = [
    path('', include(router.urls)),
]
