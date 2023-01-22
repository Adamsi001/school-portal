from django.db import models

from core.models import Session
from users.models import Lecturer, Student

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=60)
    code = models.CharField(max_length=10)
    
    description = models.CharField(max_length=300)
    semester = models.IntegerField()
    
    lecturers = models.ManyToManyField(Lecturer, related_name="courses")
    
    is_active = models.BooleanField(default=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, related_name='course_registrations', on_delete=models.CASCADE)    

    session = models.ForeignKey(Session, related_name='course_registrations', on_delete=models.CASCADE)    
    semester = models.IntegerField()
    
    courses = models.ManyToManyField(Course, related_name="registrations")

    is_approved = models.BooleanField(default=True)
    date_approved = models.DateField(blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)


    class Meta:
        verbose_name = 'Course Registration'
        verbose_name_plural = 'Courses Registrations'

    def __str__(self):
        return f"{self.student} - {self.session} - {self.semester}"

