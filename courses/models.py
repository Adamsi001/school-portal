from django.db import models

from users.models import Lecturer

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=60)
    code = models.CharField(max_length=10)
    
    description = models.CharField(max_length=300)
    semester = models.IntegerField()
    
    lecturers = models.ManyToManyField(Lecturer)
    
    is_active = models.BooleanField(default=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title
