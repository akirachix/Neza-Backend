from rest_framework import serializers
from dataUpload.models import DataUpload,ExtractedData
from user_authentication.models import UserProfile
from dashboard.models import Dashboard
from stagetracking.models import OrganizationStageTracking
from stagetracking.models import OrganizationStage
from locations.models import Locations


class StageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStageTracking
        fields="__all__"

class OrgStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationStageTracking
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['locations'] = [location.name for location in instance.locations.all()]
        return data




class DataUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUpload
        fields = '__all__'


class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(required=False)  # Add this line

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','org_type', 'website', 'phone_number','image']

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dashboard
        fields="__all__"

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations  
        fields = "__all__"  

