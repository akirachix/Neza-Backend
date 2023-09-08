from django.shortcuts import render
from rest_framework.views import APIView
from stagetracking.models import OrganizationStageTracking
from rest_framework.response import Response
from api.serializers import StageTrackingSerializer
from rest_framework import status

# Create your views here.
class StageTrackingListView(APIView):
    def get(self, request):
        stagetracking =OrganizationStageTracking.objects.all() 
        serializer = StageTrackingSerializer(stagetracking, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StageTrackingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Stage tracking created successfully",status=status.HTTP_201_CREATED)
        
        return Response("error while created stage tracking",status=status.HTTP_400_BAD_REQUEST)

class StageTrackingDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            stagetracking = OrganizationStageTracking.objects.get(id=id)
            serializer = StageTrackingSerializer(stagetracking)
            return Response(serializer.data)
        except OrganizationStageTracking.DoesNotExist:
            return Response("Stage tracking not found", status=status.HTTP_404_NOT_FOUND)
    
    
    def put(self,request,id,format=None):
         try:
            stagetracking = OrganizationStageTracking.objects.get(id=id)
            serializer = StageTrackingSerializer(stagetracking, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Stage tracking updated successfully", status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         except OrganizationStageTracking.DoesNotExist:
            return Response("Stage tracking not found", status=status.HTTP_404_NOT_FOUND)
       
    
    def delete(self,request,id,format=None):
        try:
            stagetracking = OrganizationStageTracking.objects.get(id=id)
            stagetracking.delete()
            return Response("Stage tracking successfully deleted", status=status.HTTP_204_NO_CONTENT)
        except OrganizationStageTracking.DoesNotExist:
            return Response("Stage tracking not found", status=status.HTTP_404_NOT_FOUND)
        
    

