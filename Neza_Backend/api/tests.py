
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dataUpload.models import ExtractedData
from .serializers import ExtractedDataSerializer
from django.http import Http404
from stagetracking.models import OrganizationStageTracking
from stagetracking import O
from api.serializers import StageTrackingSerializer
from django.test import TestCase
from django.urls import reverse

class ExtractedDataDetailView(APIView):
    def get_object(self, pk):
        try:
            return ExtractedData.objects.get(pk=pk)
        except ExtractedData.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        extracted_data = self.get_object(pk)
        serializer = ExtractedDataSerializer(extracted_data)
        return Response(serializer.data)

    def delete(self, request, pk):
        extracted_data = self.get_object(pk)
        extracted_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
newdata= {
        "id": 4,
        "organizationName": "UNEAP Organization",
        "stage_name": "Testing",
        "description": "We are currently on the testing stage calling upon organizations to join us",
        "start_date": "2023-09-07",
        "end_date": "2023-09-29"
    }

class StageTrackingListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_stage_tracking_list(self):
        url = reverse('stage-tracking-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_stage_tracking(self):
        url = reverse('stage-tracking-list')
        data = {
            
             "organizationName": "UNEAP Org",
             "stage_name": "Planning",
             "description": "currently in planning phase",
             "start_date": "2023-02-01",
           "end_date": "2023-02-28",
#          
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class StageTrackingDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.stage_tracking = OrganizationStageTracking.objects.create(
         **newdata
        )

    def test_get_stage_tracking_detail(self):
        url = reverse('stage-tracking-detail', args=[self.stage_tracking.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_stage_tracking(self):
        url = reverse('stage-tracking-detail', args=[self.stage_tracking.id])
        data = {
            
        "id": 4,
        "organizationName": "UNECSO Organization",
        "stage_name": "Testing",
        "description": "We are currently on the testing stage calling upon organizations to join us",
        "start_date": "2023-09-07",
        "end_date": "2023-09-29"
    
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_stage_tracking(self):
        url = reverse('stage-tracking-detail', args=[self.stage_tracking.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

   

     

    

    
