from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from stagetracking.models import OrganizationStageTracking
from api.serializers import StageTrackingSerializer
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
            
             "organizationName": "New Org",
             "stage_name": "Planning",
             "description": "New description",
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

   

     

    

    