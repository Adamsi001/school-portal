from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm

from .models import BaseUser

class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = BaseUser
        fields = '__all__'


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = BaseUser
        fields = '__all__'

