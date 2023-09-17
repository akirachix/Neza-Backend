from django.test import TestCase
from dataUpload.models import DataUpload, ExtractedData

class DataUploadTests(TestCase):
    def test_create_data_upload(self):
        data_upload = DataUpload.objects.create(
            file="test.csv",
            file_name="Test File",
            file_upload_status="Progress"
        )
        self.assertEqual(DataUpload.objects.count(), 1)
        self.assertEqual(data_upload.file, "test.csv")
        self.assertEqual(data_upload.file_name, "Test File")
        self.assertEqual(data_upload.file_upload_status, "Progress")

class ExtractedDataTests(TestCase):
    def test_create_extracted_data(self):
        extracted_data = ExtractedData.objects.create(
            location="Test Location",
            sources_of_water=1,
            proximity_to_industries="Test Industries",
            number_of_garages_in_area=5,  
            proximity_to_dumpsite="Test Dumpsite",
            presence_of_open_sewage=0,
            past_cases_of_lead_poisoning=10,
            women_and_children_population=50,
            file_hash="test_hash"
        )
        self.assertEqual(ExtractedData.objects.count(), 1)
        self.assertEqual(extracted_data.location, "Test Location")
        self.assertEqual(extracted_data.sources_of_water, 1)
        self.assertEqual(extracted_data.proximity_to_industries, "Test Industries")
        self.assertEqual(extracted_data.number_of_garages_in_area, 5) 
        self.assertEqual(extracted_data.proximity_to_dumpsite, "Test Dumpsite")
        self.assertEqual(extracted_data.presence_of_open_sewage, 0)
        self.assertEqual(extracted_data.past_cases_of_lead_poisoning, 10)
        self.assertEqual(extracted_data.women_and_children_population, 50)
        self.assertEqual(extracted_data.file_hash, "test_hash")