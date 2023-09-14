from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('org_type', 'website', 'phone_number','date_created', 'date_updated')

admin.site.register(UserProfile, UserProfileAdmin)