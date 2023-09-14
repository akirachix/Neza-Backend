from rest_framework import serializers
from user_authentication.models import UserProfile
from dashboard.models import Dashboard


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','org_type', 'website', 'phone_number']



class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dashboard
        fields="__all__"
