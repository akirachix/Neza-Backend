from rest_framework import serializers
from dataUpload.models import DataUpload,ExtractedData

class DataUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUpload
        fields = '__all__'


class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = '__all__'


from stagetracking.models import OrganizationStageTracking,OrganizationStage

class StageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStageTracking
        fields="__all__"

class OrgStageSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStage
        fields="__all__"
