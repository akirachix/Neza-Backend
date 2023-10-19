from django.db import models
from user_authentication.models import UserProfile
from locations.models import Locations
STAGENAMES=(
            ("Planning", "Planning"),
            ("Testing", "Testing"),
            ("Treating", "Treating"), )
class OrganizationStageTracking(models.Model):
   
    organizationName=models.OneToOneField(UserProfile,on_delete=models.CASCADE,unique=True)
    locations = models.ManyToManyField(Locations)
    stage_name = models.CharField(max_length=255,choices=STAGENAMES)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class OrganizationStage(models.Model):
    organization = models.ForeignKey(OrganizationStageTracking, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=255, choices=STAGENAMES)

  

 