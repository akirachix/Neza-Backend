from django.db import models
from django.utils import timezone
from user_authentication.models import UserProfile


class DataUpload(models.Model):
    class Meta:
        verbose_name_plural = "DataUpload"

    file = models.FileField(upload_to='media/')
    file_name = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    file_upload_status = models.CharField(max_length=16, choices=[
        ('Progress', 'Progress'),
        ('uploaded', 'Uploaded'),
        ('completed', 'Completed'),
    ])
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default="")


    def __str__(self):
        return self.file_name

class ExtractedData(models.Model):
    class Meta:
        verbose_name_plural = "ExtractedData"
    # file_name = models.ForeignKey(DataUpload, on_delete=models.CASCADE,default="")
    location = models.CharField(max_length=159)
    sources_of_water = models.PositiveIntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)
    proximity_to_industries = models.CharField(max_length=255)
    number_of_garages_in_area = models.IntegerField()
    proximity_to_dumpsite = models.CharField(max_length=255)
    presence_of_open_sewage = models.PositiveIntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)
    past_cases_of_lead_poisoning = models.IntegerField()  
    women_and_children_population = models.IntegerField()  
    file_hash = models.CharField(max_length=32) 


    def __str__(self):
        return f"Data extracted at {self.location}"
