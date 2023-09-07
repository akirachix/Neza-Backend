from django.db import models

# Create your models here.

#This model generates maps that display lead prediction results geographically
#these are the variables used to assertain highly affected areas

class Dashboard(models.Model):
    location = models.CharField(max_length=32)
    no_of_industries = models.IntegerField()
    is_borehole = models.BooleanField()
    population= models.BigIntegerField()
    
class Meta:
    verbose_name_plural = "Dashboard"