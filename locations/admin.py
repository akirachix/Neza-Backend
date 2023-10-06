from django.contrib import admin

from .models import Locations

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'lat', 'lng')

admin.site.register(Locations,LocationAdmin)






