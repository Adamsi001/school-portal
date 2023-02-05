from django.db import models

from users.models import BaseUser

# Create your models here.

class Announcement(models.Model):

    subject = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)

    created_by = models.ForeignKey(BaseUser, related_name='myAnnouncements', on_delete=models.CASCADE)
    sent_to = models.ManyToManyField(BaseUser, related_name='announcements', blank=True)
    seen_by = models.ManyToManyField(BaseUser, related_name='read_announcements', blank=True)

    is_active = models.BooleanField(default=True)
    
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Announcement'
        verbose_name_plural = 'Announcements'