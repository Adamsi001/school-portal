from rest_framework import viewsets

from .models import Admin, BaseUser as User, Lecturer, Staff, Student, StudentAdviser
from .serializers import AdminSerializer, LecturerSerializer, StaffSerializer, StudentAdviserSerializer, StudentSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = []

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = []

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = []

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = []

class StudentAdviserViewSet(viewsets.ModelViewSet):
    queryset = StudentAdviser.objects.all()
    serializer_class = StudentAdviserSerializer
    permission_classes = []
