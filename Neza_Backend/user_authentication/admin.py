from django.contrib import admin
from .models import UserProfile
from .models import Account


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('org_type', 'image','website', 'phone_number','date_created', 'date_updated')

admin.site.register(UserProfile, UserProfileAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Account, AccountAdmin)