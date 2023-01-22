from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from django.contrib.auth.base_user import BaseUserManager as DjangoBaseUserManager

from faculties.models import Faculty, Department
from core.models import Level

from .utils import generateUserID

ADMIN_ENUM_VALUE = 'admin'

#################################################
# BASE USER

class BaseUserManager(DjangoBaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('user_type', ADMIN_ENUM_VALUE)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class BaseUser(AbstractBaseUser, PermissionsMixin):
    class UserTypes(models.TextChoices):
        STUDENT = 'student', 'student'
        STAFF = 'staff', 'staff'
        ADMIN = ADMIN_ENUM_VALUE, ADMIN_ENUM_VALUE

    class StaffTypes(models.TextChoices):
        LECTURER = 'lecturer', 'lecturer'
        STUDENT_ADVISER = 'student_adviser', 'student adviser'
        OTHERS = 'other', 'other'
    
    class GenderTypes(models.TextChoices):
        MALE = 'male', 'male'
        FEMALE = 'female', 'female'

    user_id = models.CharField(unique=True, max_length=120, default=generateUserID)

    user_type = models.CharField(
        max_length=30, default=UserTypes.STUDENT, choices=UserTypes.choices)

    gender = models.CharField(
        max_length=30, choices=GenderTypes.choices)

    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)

    faculty = models.ForeignKey(Faculty, related_name='students', on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey(Level, related_name='students', on_delete=models.CASCADE, blank=True, null=True)
    matric_number = models.CharField(max_length=20, blank=True, null=True)
    
    is_staff = models.BooleanField(default=False) #django's default field for identifying admins

    staff_type = models.CharField(
        max_length=30, choices=StaffTypes.choices, blank=True, null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = BaseUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        while not self.id:
            while not self.user_id or BaseUser.objects.filter(user_id=self.user_id).exists():
                self.id = generateUserID()

            return super().save(*args, **kwargs)


#################################################
# ADMIN

class AdminManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return BaseUser.objects.filter(user_type=BaseUser.UserTypes.ADMIN)

class Admin(BaseUser):
    user_type = BaseUser.UserTypes.ADMIN
    objects = AdminManager()

    class Meta:
        proxy: True

#################################################
# STUDENT

class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return BaseUser.objects.filter(user_type=BaseUser.UserTypes.STUDENT)

class Student(BaseUser):
    user_type = BaseUser.UserTypes.STUDENT
    objects = StudentManager()

    class Meta:
        proxy: True


#################################################
# STAFF

class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return BaseUser.objects.filter(user_type=BaseUser.UserTypes.STAFF)

class Staff(BaseUser):
    user_type = BaseUser.UserTypes.STAFF
    staff_type = BaseUser.StaffTypes.OTHERS
    objects = StaffManager()

    class Meta:
        proxy: True
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

# ADVISER
class StudentAdviserManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return Staff.objects.filter(user_type=BaseUser.UserTypes.STAFF, staff_type=BaseUser.StaffTypes.STUDENT_ADVISER)

class StudentAdviser(BaseUser):
    user_type = BaseUser.UserTypes.STAFF
    staff_type = BaseUser.StaffTypes.STUDENT_ADVISER
    objects = StudentAdviserManager()

    class Meta:
        proxy: True

# LECTURER
class LecturerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return Staff.objects.filter(user_type=BaseUser.UserTypes.STAFF, staff_type=BaseUser.StaffTypes.LECTURER)

class Lecturer(BaseUser):
    user_type = BaseUser.UserTypes.STAFF
    staff_type = BaseUser.StaffTypes.LECTURER
    objects = LecturerManager()

    class Meta:
        proxy: True
