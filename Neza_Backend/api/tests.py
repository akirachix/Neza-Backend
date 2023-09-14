from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from dataUpload.models import ExtractedData

class ExtractedDataTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_file(self):
        test_csv_data = "location,sources of water,proximity to industries,number of garages in an area," \
                        "proximity to dumpsite,presence of open sewage,past cases of lead poisoning,women and children population\n" \
                        "Test Location,Yes,123,45,Yes,No,0,678\n"
        
        response = self.client.post('/upload/', {'file': test_csv_data}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ExtractedData.objects.count(), 1)
        extracted_data = ExtractedData.objects.first()
        self.assertEqual(extracted_data.location, "Test Location")

    def test_extracted_data_list_view(self):
        ExtractedData.objects.create(location="Location 1", sources_of_water=1)
        ExtractedData.objects.create(location="Location 2", sources_of_water=0)

        response = self.client.get('/extracted-data/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_extracted_data_detail_view(self):
        extracted_data = ExtractedData.objects.create(location="Location 1", sources_of_water=1)

        response = self.client.get(f'/extracted-data/{extracted_data.id}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['location'], "Location 1")

    def test_extracted_data_delete_view(self):
        extracted_data = ExtractedData.objects.create(location="Location 1", sources_of_water=1)

        response = self.client.delete(f'/extracted-data/{extracted_data.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ExtractedData.objects.count(), 0)
