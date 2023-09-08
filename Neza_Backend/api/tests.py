from django.test import TestCase
# from rest_framework.test import APIClient
# from dashboard.models import Dashboard
# from .serializers import DashboardSerializer
# # Create your tests here.

# class DashboardViewTest(TestCase):
#     def setUp(self):
#         self.Nakuru = Dashboard.objects.create(location ="Nakuru", no_of_industries= 5, is_borehole= True, population= 3000000000)
#         self.Nairobi = Dashboard.objects.create(location ="Nairobi", no_of_industries=2,is_borehole= True, population= 3000000000)
#         response = self.client.get(reversed('api'))
#         self.client = APIClient()

#     def test_dashboard_list_view(self):
#         response = self.client.get('dashboard/')
#         # self.assertEqual(response.status_code, 200)
#         # self.assertIsInstance(response, list)
#         expected_data = DashboardSerializer([self.Nakuru, self.Nakuru], many=True)
#         self.assertEqual(response, expected_data)

#     def test_dashboard_detail_view(self):
#         response = self.client.get(f'dashboarddetails/<int:id>/{self.Nairobi.id}/')
#         # self.assertEqual(response.status_code, 200)
#         expected_data = DashboardSerializer(self.Nakuru)
#         self.assertEqual(response, expected_data)

  
