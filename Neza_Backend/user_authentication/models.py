from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    org_type = models.CharField(max_length=20)
    website = models.URLField()
    phone_number = PhoneNumberField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', default="")
    def __str__(self):
        return self.username
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        account, created = Account.objects.get_or_create(user=self)
        account.save()

class Account(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='account', null=True)
   

    def __str__(self):
        return str(self.user)
    