from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    is_teacher = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10, unique=True)
    user_image = models.ImageField(default='default.jpg',
        upload_to='user_profile_images/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
