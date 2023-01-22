from rest_framework.serializers import ModelSerializer

from .models import BaseUser as User, Admin, Lecturer, Staff, Student, StudentAdviser


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email',  'user_id', 'first_name', 'middle_name', 'last_name', 'gender', 'is_active', 'is_staff', "user_type", "staff_type", 'faculty', 'department', 'level', 'matric_number', )


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ('email',  'user_id', 'first_name', 'middle_name', 'last_name', 'gender', 'is_active', 'is_superuser')

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('email',  'user_id', 'first_name', 'middle_name', 'last_name', 'gender', 'is_active', 'faculty', 'department', 'level', 'matric_number',)

class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ('email',  'user_id', 'first_name', 'middle_name', 'last_name', 'gender', 'is_active', 'staff_type',)

class LecturerSerializer(ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('email',  'user_id', 'first_name', 'middle_name', 'last_name',  'gender', 'is_active', 'faculty', 'department',)

class StudentAdviserSerializer(ModelSerializer):
    class Meta:
        model = StudentAdviser
        fields = ('email',  'user_id', 'first_name', 'middle_name', 'last_name', 'gender', 'is_active', 'faculty', 'department', 'level',)
