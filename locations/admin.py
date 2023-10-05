from django.contrib import admin
from .models import location

class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "lat", "lng")

admin.site.register(location, LocationAdmin)
