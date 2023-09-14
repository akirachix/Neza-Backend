from django.shortcuts import render
from rest_framework.views import APIView
from dashboard.models import Dashboard
from .serializers import DashboardSerializer
from rest_framework.response import Response

# Create your views here.
class DashboardListView(APIView):
    def get(self,request):
        location_details = Dashboard.objects.all()
        serializer = DashboardSerializer(location_details, many=True)
        return Response(serializer.data)
    
