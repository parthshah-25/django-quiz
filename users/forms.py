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



class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'block appearance-none w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            },
        ),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'block appearance-none w-full px-3 py-2 border border-gray-300 rounded-md placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm',
            },
        ),
    )
