from rest_framework.serializers import ModelSerializer

from .models import Course, CourseRegistration, CourseResult, Result


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class CourseRegistrationSerializer(ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = "__all__"

class CourseResultSerializer(ModelSerializer):
    class Meta:
        model = CourseResult
        fields = "__all__"

class ResultSerializer(ModelSerializer):
    courses = CourseResultSerializer(many=True)
    class Meta:
        model = Result
        fields = ('student', 'session', 'semester', 'is_approved', 'date_approved', 'date_created', "courses",)
