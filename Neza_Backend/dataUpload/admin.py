from django.contrib import admin
from .models import DataUpload,ExtractedData



# Register your models here.

class DataUploadAdmin(admin.ModelAdmin):
    list_display = ('file','file_name', 'date_uploaded', 'file_upload_status')

admin.site.register(DataUpload,DataUploadAdmin)


class ExtractedDataAdmin(admin.ModelAdmin):
    list_display = ('location','sources_of_water','proximity_to_industries','number_of_garages_in_area','proximity_to_dumpsite','presence_of_open_sewage','past_cases_of_lead_poisoning','women_and_children_population')

admin.site.register(ExtractedData,ExtractedDataAdmin)

