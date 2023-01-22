from rest_framework.serializers import ModelSerializer

from .models import Course, CourseRegistration


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseRegistrationSerializer(ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = "__all__"
