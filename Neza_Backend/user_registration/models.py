from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    org_type = models.CharField(max_length=20)
    website = models.URLField()
    phone_number = PhoneNumberField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'User_Registration_userprofile'
        