from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)