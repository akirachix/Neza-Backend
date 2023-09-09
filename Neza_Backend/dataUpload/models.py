from django.db import models
from django.utils import timezone
import csv

# Create your models here.
class DataUpload(models.Model):
    class Meta:
        verbose_name_plural = "dataUpload"

    file = models.FileField()
    file_name = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    file_upload_status = models.CharField(max_length=16,choices=[
        ('pending', 'pending'),
        ('uploaded', 'uploaded'),
    ])

    def __str__(self):
        return self.file_name
    




class ExtractedData(models.Model):
    location=models.CharField(max_length=159)
    sources_of_water = models.BooleanField(
        help_text="Check this box if your source of water is borehole"
    )
    proximity_to_industries = models.CharField(max_length=255)
    number_of_garages_in_area = models.IntegerField()
    proximity_to_dumpsite = models.CharField(max_length=255)
    presence_of_open_sewage = models.BooleanField(
        help_text="Check this box if there is an open sewage in your location"
    )
    past_cases_of_lead_poisoning = models.CharField(max_length=255)
    women_and_children_population = models.IntegerField()


    def __str__(self):
        return f"Data extracted at {self.location}"
    










































