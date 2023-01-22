from django.db import models

class Faculty(models.Model):
    title = models.CharField(max_length=20)
    abbrevation = models.CharField(max_length=20)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=20)
    abbrevation = models.CharField(max_length=20)
    short_code = models.CharField(max_length=20)
    Faculty = models.ForeignKey('Faculty', related_name='departments', on_delete=models.CASCADE)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.title
