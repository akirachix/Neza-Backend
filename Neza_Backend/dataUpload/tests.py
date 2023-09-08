from django.test import TestCase
from .models import DataUpload

# # Create your tests here.

from django.test import TestCase
from django.utils import timezone
from .models import DataUpload

class DataUploadTestCase(TestCase):
    def setUp(self):
        self.uploaded_file = DataUpload.objects.create(
            file_name='example.txt',
            file_type='text',
            date_uploaded=timezone.now(),
            file_upload_status='success'
        )

    def test_data_upload_str_representation(self):
        self.assertEqual(str(self.uploaded_file), 'example.txt')

    def test_data_upload_fields(self):
        uploaded_file = DataUpload.objects.get(file_name='example.txt')

        self.assertEqual(uploaded_file.file_name, 'example.txt')
        self.assertEqual(uploaded_file.file_type, 'text')
        self.assertEqual(uploaded_file.file_upload_status, 'success')

    def test_data_upload_date_uploaded(self):
        uploaded_file = DataUpload.objects.get(file_name='example.txt')

        self.assertTrue(timezone.is_aware(uploaded_file.date_uploaded))

