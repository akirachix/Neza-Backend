from django.db import models
# Create your models here.
from django.db import models

class Locations(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name 