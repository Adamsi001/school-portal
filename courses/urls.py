from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseRegistrationViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-registrations', CourseRegistrationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
