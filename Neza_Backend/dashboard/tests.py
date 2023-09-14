from django.test import TestCase
from .models import Dashboard

class DashboardModelTest(TestCase):
    def setUp(self):
        self.dashboard = Dashboard.objects.create(
            location="Nairobi",
            no_of_industries=5,
            is_borehole=True,
            population=1000,
        )

    def test_dashboard_str_method(self):
        expected_str = "Nairobi"


    def test_default_values(self):
        dashboard = Dashboard.objects.create(location="Nairobi", no_of_industries=5, is_borehole=True, population=1000)
        self.assertEqual(dashboard.no_of_industries, 5)
        self.assertEqual(dashboard.is_borehole, True)
        self.assertEqual(dashboard.population, 1000)

    def test_model_fields(self):
        self.assertIsInstance(self.dashboard.location, str)
        self.assertIsInstance(self.dashboard.no_of_industries, int)
        self.assertIsInstance(self.dashboard.is_borehole, bool)
        self.assertIsInstance(self.dashboard.population, int)
