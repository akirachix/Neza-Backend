from rest_framework import serializers
from stagetracking.models import OrganizationStageTracking

class StageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStageTracking
        fields="__all__"
