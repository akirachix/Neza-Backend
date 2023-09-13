from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from stagetracking.models import OrganizationStageTracking,OrganizationStage
from api.serializers import StageTrackingSerializer,OrgStageSerializer
from django.db.models import Q
from django.http import JsonResponse

class OrganizationsInStageView(ListAPIView):
    serializer_class = OrgStageSerializer
    def get_queryset(self):
        stage_name = self.kwargs['stage_name']
        try:
           
            organizations_in_stage = OrganizationStage.objects.filter(
                Q(stage_name__iexact=stage_name)
            )
            return organizations_in_stage
        except OrganizationStage.DoesNotExist:
           
            error_message = f"No organizations found for stage '{stage_name}'."
            return JsonResponse({'error': error_message}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = self.serializer_class(queryset, many=True).data
        result_data = []
        for item in data:
            organization_id = item['organization']
            organization = OrganizationStageTracking.objects.get(id=organization_id)
            item['organization_name'] = organization.organizationName
            result_data.append(item)

        return JsonResponse(result_data, safe=False, status=status.HTTP_200_OK)

    

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
    

