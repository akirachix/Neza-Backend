
# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from dataUpload.models import DataUpload
from.serializers import DataUploadSerializer
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

# customer apis
class DataUploadListView(APIView):
    def get(self, request):
        dataUploads = DataUpload.objects.all() 
        serializer = DataUploadSerializer(dataUploads, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=DataUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class DataUploadDetailView(APIView):
    def get(self,request,id,format=None):
        dataUpload=DataUpload.objects.get(id=id)
        serializer=DataUploadSerializer(dataUpload)
        return Response(serializer.data)
    
    def put(self,request,id,format=None):
        dataUpload=DataUpload.objects.get(id=id)
        serializer=DataUploadSerializer(dataUpload,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        dataUpload=DataUpload.objects.get(id=id)
        dataUpload.delete()
        return Response("file successfully deleted",status=status.HTTP_204_NO_CONTENT)
    


