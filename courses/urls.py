from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CourseRegistrationViewSet, CourseResultViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-registrations', CourseRegistrationViewSet)
router.register(r'course-results', CourseResultViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
