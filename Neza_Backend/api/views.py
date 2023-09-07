from django.shortcuts import render
from rest_framework.views import APIView
from stagetracking.models import OrganizationStageTracking
from rest_framework.response import Response
from .serializers import StageTrackingSerializer
from rest_framework import status

# Create your views here.
class StageTrackingListView(APIView):
    def get(self, request):
        stagetracking =OrganizationStageTracking.objects.all()  # Corrected variable name
        serializer = StageTrackingSerializer(stagetracking, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StageTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StageTrackingDetailView(APIView):
    def get(self,request,id,format=None):
        stagetracking=OrganizationStageTracking.objects.get(id=id)
        serializer=StageTrackingSerializer(stagetracking)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        customer=OrganizationStageTracking.objects.get(id=id)
        serializer=StageTrackingSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        customer=OrganizationStageTracking.objects.get(id=id)
        customer.delete()
        return Response("stage tracking successfully deleted",status=status.HTTP_204_NO_CONTENT)
    
# Create your views here.
