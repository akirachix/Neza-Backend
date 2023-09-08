from django.test import TestCase
from .models import DataUpload

# # Create your tests here.

from django.test import TestCase
from django.utils import timezone
from .models import DataUpload

class DataUploadTestCase(TestCase):
    def setUp(self):
        self.uploaded_file = DataUpload.objects.create(
            file_name='example.csv',
            date_uploaded=timezone.now(),
            file_upload_status='uploaded'
        )

    def test_data_upload_str_representation(self):
        self.assertEqual(str(self.uploaded_file), 'example.csv')

    def test_data_upload_fields(self):
        uploaded_file = DataUpload.objects.get(file_name='example.csv')

        self.assertEqual(uploaded_file.file_name, 'example.csv')
        self.assertEqual(uploaded_file.file_upload_status, 'uploaded')

    def test_data_upload_date_uploaded(self):
        uploaded_file = DataUpload.objects.get(file_name='example.csv')

        self.assertTrue(timezone.is_aware(uploaded_file.date_uploaded))

