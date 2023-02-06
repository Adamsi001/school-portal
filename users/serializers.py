from rest_framework.serializers import ModelSerializer

from .models import BaseUser as User, Admin, Lecturer, Staff, Student, StudentAdviser


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email',  'user_id', 'first_name', 'middle_name', 'last_name', 'gender', 'is_active', 'is_lecturer',
                  "is_student_adviser", "user_type", "staff_type", 'faculty', 'department', 'level', 'matric_number', )


class AdminSerializer(ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email',  'user_id', 'first_name', 'middle_name',
                  'last_name', 'gender', 'is_active', 'is_superuser')


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'email',  'user_id', 'first_name', 'middle_name', 'last_name',
                  'gender', 'is_active', 'faculty', 'department', 'level', 'matric_number',)


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'email',  'user_id', 'first_name', 'middle_name', 'last_name',
                  'is_lecturer', "is_student_adviser", 'gender', 'is_active', 'staff_type',)


class LecturerSerializer(ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'email',  'user_id', 'first_name', 'middle_name',
                  'last_name',  'gender', 'is_active', 'is_lecturer', "is_student_adviser", 'faculty', 'department',)


class StudentAdviserSerializer(ModelSerializer):
    class Meta:
        model = StudentAdviser
        fields = ('id', 'email',  'user_id', 'first_name', 'middle_name',
                  'last_name', 'gender', 'is_active', 'is_lecturer', "is_student_adviser", 'faculty', 'department', 'level',)
