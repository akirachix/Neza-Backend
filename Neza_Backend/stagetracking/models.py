from django.db import models

class OrganizationStageTracking(models.Model):
    STAGENAMES=(
            ("Planning", "Planning"),
            ("Testing", "Testing"),
            ("Treating", "Treating"), )
    organizationName=models.CharField(max_length=32)
    stage_name = models.CharField(max_length=255,choices=STAGENAMES)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    

  

 