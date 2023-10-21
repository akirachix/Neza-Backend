from django.db import models
from django.utils import timezone
# from user_authentication.models import UserProfile


class DataUpload(models.Model):
    class Meta:
        verbose_name_plural = "DataUpload"

    file = models.FileField(upload_to='media/')
    file_name = models.CharField(max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    # owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE,default="")


    def __str__(self):
        return self.file_name

class ExtractedData(models.Model):
    class Meta:
        verbose_name_plural = "ExtractedData"
  
    location = models.CharField(max_length=159)
    sources_of_water = models.CharField(max_length=32,default="")
    proximity_to_industries = models.CharField(max_length=255,default="")
    number_of_garages_in_area = models.IntegerField(default=0)
    proximity_to_dumpsite = models.CharField(max_length=255,default="")
    presence_of_open_sewage = models.CharField(max_length=32,default="")
    past_cases_of_lead_poisoning = models.IntegerField(default=0)  
    women_and_children_population = models.IntegerField(default=0) 
    file_hash = models.CharField(max_length=32) 
    lead_blood_levels=models.CharField(max_length=32, default="")
    file_name=models.CharField(max_length=32, default="")

 

    def __str__(self):
        return f"Data extracted at {self.location}"
