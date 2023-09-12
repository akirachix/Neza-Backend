from django.urls import path
from.views import DataUploadListView,DataUploadDetailView,upload_file,ExtractedDataListView,ExtractedDataDeleteView,ExtractedDataUpdateFileView

urlpatterns=[
    path("dataUploads/", DataUploadListView.as_view(),name="data_upload_list_view"),
    path("dataUploads/<int:id>/", DataUploadDetailView.as_view(),name="data_upload_detail_view"),
    path('upload/', upload_file, name='upload_file'),
    path('extracteddata/', ExtractedDataListView.as_view(), name='extracted_data_list_view'),
    path('extracteddata/<int:pk>/', ExtractedDataDeleteView.as_view(), name='extracted_data_delete_view'),
    path('extracteddata/<int:pk>/updatefile/', ExtractedDataUpdateFileView.as_view(), name='extracted_data_update_file_view'),



]