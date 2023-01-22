from rest_framework import viewsets

from .models import Course, CourseRegistration, CourseResult
from .serializers import CourseRegistrationSerializer, CourseResultSerializer, CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

class CourseRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = []

class CourseResultViewSet(viewsets.ModelViewSet):
    queryset = CourseResult.objects.all()
    serializer_class = CourseResultSerializer
    permission_classes = []
