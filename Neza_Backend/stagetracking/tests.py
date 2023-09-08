from django.test import TestCase
from .models import OrganizationStageTracking

class OrganizationStageTrackingTestCase(TestCase):
    def test_organization_creation(self):
        org = OrganizationStageTracking.objects.create(
            organizationName="Example Org",
            stage_name="Planning",
            description="This is an example organization",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        self.assertEqual(org.organizationName, "Example Org")
        self.assertEqual(org.stage_name, "Planning")

