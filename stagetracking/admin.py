from django.contrib import admin
from .models import OrganizationStageTracking,OrganizationStage

class OrganizationStageTrackingAdmin(admin.ModelAdmin):
    list_display = ("organizationName", "stage_name", "description", "start_date", "end_date",)

admin.site.register(OrganizationStageTracking, OrganizationStageTrackingAdmin)

class OrgStageAdmin(admin.ModelAdmin):
    list_display = ("stage_name",)
admin.site.register(OrganizationStage,OrgStageAdmin)





