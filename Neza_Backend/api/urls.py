from django.urls import path
from.views import DataUploadListView,DataUploadDetailView,upload_file

urlpatterns=[
    path("dataUploads/", DataUploadListView.as_view(),name="data_upload_list_view"),
    path("dataUploads/<int:id>/", DataUploadDetailView.as_view(),name="data_upload_detail_view"),
    path('upload/', upload_file, name='upload_file'),


]