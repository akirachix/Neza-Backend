from django.test import TestCase
from .models import OrganizationStageTracking,OrganizationStage

class OrganizationStageTrackingTestCase(TestCase):
    def test_organization_creation(self):
        org = OrganizationStageTracking.objects.create(
            organizationName="UON Org",
            stage_name="Planning",
            description="This is an example organization",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        self.assertEqual(org.organizationName, "UON Org")
        self.assertEqual(org.stage_name, "Planning")

    def test_unique_organization_name(self):
        
        org1 = OrganizationStageTracking.objects.create(
            organizationName="Neza",
            stage_name="Testing",
            description="This is a duplicate organization",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        org2 = OrganizationStageTracking(
            organizationName="Neza",
            stage_name="Treating",
            description="This is another duplicate organization",
            start_date="2023-01-01",
            end_date="2023-12-31",
        )
        with self.assertRaises(Exception) as context:
            org2.save()

        
        self.assertTrue(
            "organizationName" in str(context.exception),
            "Organization name should be unique but is not enforced.",
        )


