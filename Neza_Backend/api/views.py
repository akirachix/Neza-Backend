from django.shortcuts import render
from rest_framework.views import APIView
from dashboard.models import Dashboard
from .serializers import DashboardSerializer
from rest_framework.response import Response

# Create your views here.
# customer apis
class DashboardListView(APIView):
    def get(self,request):
        location_details = Dashboard.objects.all()
        serializer = DashboardSerializer(location_details, many=True)
        return Response(serializer.data)
    
class DashboardView(APIView):
    def get(self,request,id,format=None):
        location_details=Dashboard.objects.all()
        serializer=DashboardSerializer(location_details)
        return Response(serializer.data)