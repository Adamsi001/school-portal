from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.serializers import UserSerializer

from .models import Announcement


class AnnouncementSerializer(ModelSerializer):
    created_by = SerializerMethodField()

    class Meta:
        model = Announcement
        fields = "__all__"

    def get_created_by(self, announcement):
        return UserSerializer(announcement.created_by).data
