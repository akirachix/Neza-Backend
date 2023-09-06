from django.contrib import admin
from .models import Dashboard

# Register your models here.

class Dashboard(admin.ModelAdmin):
    display = ("location", "no_of_industries", "is_borehole ", "population" )
    
admin.site.register(Dashboard)
