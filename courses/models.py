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

class Result(models.Model):
    student = models.ForeignKey(Student, related_name='results', on_delete=models.CASCADE)    

    session = models.ForeignKey(Session, related_name='results', on_delete=models.CASCADE)    
    semester = models.IntegerField()
    
    is_approved = models.BooleanField(default=True)
    date_approved = models.DateField(blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.session} - {self.semester}"

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'

MAX_CA_SCORE = 40.00
MAX_EXAM_SCORE = 60.00
class CourseResult(models.Model):
    student = models.ForeignKey(Student, related_name='course_results', on_delete=models.CASCADE)    
    course = models.ForeignKey(Course, related_name='results', on_delete=models.CASCADE)

    resultSheet = models.ForeignKey(Result, related_name='courses', on_delete=models.CASCADE)

    ca_score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    exam_score = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # is_approved = models.BooleanField(default=True)
    # date_approved = models.DateField(blank=True, null=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Course Result'
        verbose_name_plural = 'Courses Results'

    def __str__(self):
        return f"{self.course} - {self.student}"

    def save(self, *args, **kwargs):
        if (self.ca <= MAX_CA_SCORE) and (self.exam_score <= MAX_EXAM_SCORE):
            super().save(*args, **kwargs)
