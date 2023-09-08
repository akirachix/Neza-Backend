from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from dataUpload.models import DataUpload
from api.serializers import DataUploadSerializer

class DataUploadListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_data_upload_list(self):
        url = reverse('data_upload_list_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_data_upload(self):
        url = reverse('data_upload_list_view')
        file = SimpleUploadedFile("test_file.csv", b"file_content", content_type="text/csv")
        data = {
            'file': file,
            'file_name': 'Nakurucase.csv',
            'file_upload_status': 'uploaded'
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DataUploadDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.data_upload = DataUpload.objects.create(
            file_name="Nakurucase.csv",
            file_upload_status="uploaded",
            file=SimpleUploadedFile("test_file.csv", b"file_content", content_type="text/csv")
        )

    def test_get_data_upload_detail(self):
        url = reverse('data_upload_detail_view', args=[self.data_upload.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_data_upload(self):
        url = reverse('data_upload_detail_view', args=[self.data_upload.id])
        file = SimpleUploadedFile("updated_file.csv", b"updated_content", content_type="text/csv")
        data = {
            'file': file,
            'file_name': 'Updated_Nakurucase.csv',
            'file_upload_status': 'pending'
        }
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_data_upload(self):
        url = reverse('data_upload_detail_view', args=[self.data_upload.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

