from django.db import models
from django.utils import timezone

# Create your models here.
class DataUpload(models.Model):
    class Meta:
        verbose_name_plural = "dataUpload"

    file = models.FileField(upload_to='uploads/')
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    date_uploaded = models.DateTimeField(default=timezone.now)
    file_upload_status = models.CharField(max_length=20)

    def __str__(self):
        return self.file_name
