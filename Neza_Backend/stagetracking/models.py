from django.db import models
STAGENAMES=(
            ("Planning", "Planning"),
            ("Testing", "Testing"),
            ("Treating", "Treating"), )
class OrganizationStageTracking(models.Model):
   
    organizationName=models.CharField(max_length=32,unique=True)
    stage_name = models.CharField(max_length=255,choices=STAGENAMES)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class OrganizationStage(models.Model):
    organization = models.ForeignKey(OrganizationStageTracking, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=255, choices=STAGENAMES)

  

 