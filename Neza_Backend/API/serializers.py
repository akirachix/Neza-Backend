from rest_framework import serializers
from dataUpload.models import DataUpload

class DataUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUpload
        fields = '__all__'

