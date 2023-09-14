from django.test import TestCase
from rest_framework.test import APIClient

class DashboardListViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        
    def test_get_dashboard_list(self):
        response = self.client.get('/api/dashboard/')