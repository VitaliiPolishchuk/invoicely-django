from django.db import router
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TeamViewSet

router = DefaultRouter()
router.register("team", TeamViewSet, basename="teams")

urlpatterns = [
  path('', include(router.urls)),
]