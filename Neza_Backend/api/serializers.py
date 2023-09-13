from rest_framework import serializers
from stagetracking.models import OrganizationStageTracking,OrganizationStage

class StageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStageTracking
        fields="__all__"

class OrgStageSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStage
        fields="__all__"
