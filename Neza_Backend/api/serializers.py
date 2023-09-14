from rest_framework import serializers
from user_registration.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','org_type', 'website', 'phone_number']

