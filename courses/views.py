from rest_framework import viewsets

from .models import Course, CourseRegistration
from .serializers import CourseRegistrationSerializer, CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

class CourseRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CourseRegistration.objects.all()
    serializer_class = CourseRegistrationSerializer
    permission_classes = []
