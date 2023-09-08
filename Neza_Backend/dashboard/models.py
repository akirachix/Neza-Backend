from django.db import models

# Create your models here.
#This model generates maps that display lead prediction results geographically
#these are the variables used to assertain highly affected areas
# location: A character field to store the location with a maximum length of 32 characters.
# no_of_industries: A positive integer field that represents the number of industries, with a default value of 0.
# is_borehole: A boolean field indicating whether it's related to a borehole.
# population: A big integer field to store population data.

class Dashboard(models.Model):
    location = models.CharField(max_length=32)
    no_of_industries = models.PositiveIntegerField(default=0)
    is_borehole = models.BooleanField()
    population= models.BigIntegerField()
    
    def __str__(self):
        return self.name
    
class Meta:
    verbose_name_plural = "Dashboards"