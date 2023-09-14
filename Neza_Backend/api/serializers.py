from rest_framework import serializers
<<<<<<< HEAD
from stagetracking.models import OrganizationStageTracking,OrganizationStage

class StageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStageTracking
        fields="__all__"

class OrgStageSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStage
        fields="__all__"
=======
from dashboard.models import Dashboard


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dashboard
        fields="__all__"
>>>>>>> 931406d46d7896fb6062b2246a3ab0a3bfdd150f
