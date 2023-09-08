from django.db import models
from django.utils import timezone

# Create your models here.
class DataUpload(models.Model):
    class Meta:
        verbose_name_plural = "dataUpload"

    file = models.FileField(upload_to='media/')
    file_name = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    file_upload_status = models.CharField(max_length=16,choices=[
        ('pending', 'pending'),
        ('uploaded', 'uploaded'),
    ])

    def __str__(self):
        return self.file_name
