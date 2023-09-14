from django.contrib import admin
from .models import Dashboard

# Register your models here.

class DashboardAdmin(admin.ModelAdmin):
    display = ("location", "no_of_industries", "is_borehole ", "population" )
    
admin.site.register(Dashboard, DashboardAdmin)
