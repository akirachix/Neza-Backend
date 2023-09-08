from django.contrib import admin
from .models import DataUpload


# Register your models here.

class DataUploadAdmin(admin.ModelAdmin):
    list_display = ('file','file_name', 'date_uploaded', 'file_upload_status')

admin.site.register(DataUpload,DataUploadAdmin)


