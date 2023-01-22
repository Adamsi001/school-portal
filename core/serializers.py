from rest_framework.serializers import ModelSerializer

from .models import Session, Level


class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
        
class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"
        