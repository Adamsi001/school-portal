from rest_framework import viewsets

from django.contrib.auth import get_user_model

from .models import Announcement
from .serializers import AnnouncementSerializer

User = get_user_model()


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = []

    def get_queryset(self):
        if self.action == "list":
            return self.queryset.filter(created_by=self.request.user) | self.queryset.filter(sent_to=self.request.user)
        return super().get_queryset()

    def perform_create(self, serializer):
        user = self.request.user  # current user
        announcement = serializer.save(created_by=user)

        # automatically send student advisers' messages to all students under them
        if user.is_student_adviser:
            announcement.sent_to.add(*User.objects.filter(user_type=User.UserTypes.STUDENT,
                                     department=user.department, faculty=user.faculty, level=user.level))
        announcement.save()
