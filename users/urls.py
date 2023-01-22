from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import AdminViewSet, LecturerViewSet, StaffViewSet, StudentAdviserViewSet, StudentViewSet, UserViewSet

router = DefaultRouter()
router.register(r'all', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'student-adviser', StudentAdviserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
