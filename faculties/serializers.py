from rest_framework.serializers import ModelSerializer

from .models import Faculty, Department


class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"
        

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
        
