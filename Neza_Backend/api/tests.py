from django.test import TestCase
from rest_framework.test import APIClient
from dashboard.models import Dashboard
from .serializers import DashboardSerializer
from rest_framework import status

# Create your tests here.
class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_dashboard_list_view(self):
        response = self.client.get('dashboard_location_details/')
        self.assertEqual('Dashboard successfully displayed',response.status_code, status.HTTP_200_OK)
                