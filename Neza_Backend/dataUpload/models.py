from django.db import models
from django.utils import timezone

# Create your models here.
class DataUpload(models.Model):
    class Meta:
        verbose_name_plural = "DataUpload"

    file = models.FileField(upload_to='media/')
    file_name = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    file_upload_status = models.CharField(max_length=16,choices=[
        ('Progress', 'progress'),
        ('uploaded', 'uploaded'),
        ('completed', 'completed'),
    ])

    def __str__(self):
        return self.file_name
    

class ExtractedData(models.Model):
    class Meta:
        verbose_name_plural = "Extracted data"
    location = models.CharField(max_length=159)
    sources_of_water = models.CharField(max_length=255,blank=True, null=True)
    proximity_to_industries = models.CharField(max_length=255)
    number_of_garages_in_area = models.IntegerField()
    proximity_to_dumpsite = models.CharField(max_length=255)
    presence_of_open_sewage = models.CharField(max_length=255,blank=True, null=True)
    past_cases_of_lead_poisoning = models.CharField(max_length=255)
    women_and_children_population = models.CharField(max_length=255)

    def __str__(self):
        return f"Data extracted at {self.location}"


    









































