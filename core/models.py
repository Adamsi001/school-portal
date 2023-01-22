from django.db import models

class Session(models.Model):
    title = models.CharField(max_length=20)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'

    def __str__(self):
        return self.title

class Level(models.Model):
    title = models.CharField(max_length=20)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

    def __str__(self):
        return self.title