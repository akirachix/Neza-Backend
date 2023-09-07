from django.contrib import admin
from .models import DataUpload


# Register your models here.

class DataUploadAdmin(admin.ModelAdmin):
    list_display = ('file_name', 'file_type', 'date_uploaded', 'file_upload_status')

admin.site.register(DataUpload,DataUploadAdmin)


