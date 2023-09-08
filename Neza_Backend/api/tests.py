from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from dataUpload.models import DataUpload
from .serializers import DataUploadSerializer

class DataUploadAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.data_upload1 = DataUpload.objects.create(
            file_name='file1.txt',
            file_type='txt',
            file_upload_status='uploaded'
        )
        self.data_upload2 = DataUpload.objects.create(
            file_name='file2.csv',
            file_type='csv',
            file_upload_status='processing'
        )

    def test_get_datauploads(self):
        response = self.client.get('/api/datauploads/')  
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = DataUploadSerializer([self.data_upload1, self.data_upload2], many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_dataupload(self):
        data = {
            'file_name': 'new_file.txt',
            'file_type': 'txt',
            'file_upload_status': 'uploaded'
        }

        response = self.client.post('/api/datauploads/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(DataUpload.objects.filter(file_name='new_file.txt').exists())

    def test_update_dataupload(self):
        data = {
            'file_upload_status': 'updated'
        }

        response = self.client.put(f'/api/datauploads/{self.data_upload1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_data_upload = DataUpload.objects.get(id=self.data_upload1.id)
        self.assertEqual(updated_data_upload.file_upload_status, 'updated')

    def test_delete_dataupload(self):
        response = self.client.delete(f'/api/datauploads/{self.data_upload1.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(DataUpload.objects.filter(id=self.data_upload1.id).exists())

