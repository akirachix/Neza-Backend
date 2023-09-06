from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)

