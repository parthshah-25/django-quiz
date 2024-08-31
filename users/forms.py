from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'phone_number', 'user_image',
                  'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    user_image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'phone_number', 'user_image')
