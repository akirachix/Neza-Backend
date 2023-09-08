from django.urls import path
from.views import DataUploadListView,DataUploadDetailView

urlpatterns=[
    path("dataUploads/", DataUploadListView.as_view(),name="data_upload_list_view"),
    path("dataUploads/<int:id>/", DataUploadDetailView.as_view(),name="data_upload_detail_view"),

]