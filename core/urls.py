from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SessionViewSet,LevelViewSet

router = DefaultRouter()
router.register(r'sessions', SessionViewSet)
router.register(r'levels', LevelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
