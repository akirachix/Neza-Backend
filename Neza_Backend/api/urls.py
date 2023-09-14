# from django.urls import path
# from.views import DataUploadListView,DataUploadDetailView,upload_file,ExtractedDataListView,ExtractedDataDeleteView,ExtractedDataUpdateFileView

# urlpatterns=[
#     path("dataUploads/", DataUploadListView.as_view(),name="data_upload_list_view"),
#     path("dataUploads/<int:id>/", DataUploadDetailView.as_view(),name="data_upload_detail_view"),
#     path('upload/', upload_file, name='upload_file'),
#     path('extracteddata/', ExtractedDataListView.as_view(), name='extracted_data_list_view'),
#     path('extracteddata/<int:pk>/', ExtractedDataDeleteView.as_view(), name='extracted_data_delete_view'),
#     path('extracteddata/<int:pk>/updatefile/', ExtractedDataUpdateFileView.as_view(), name='extracted_data_update_file_view'),

# ]
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path("extracted_data/", views.ExtractedDataListView.as_view(),name="extracted_data_list_view"),
    path('extracted_data/<int:pk>/', views.ExtractedDataDetailView.as_view(), name='extracted_data_detail'),
    path('extracted_data/delete/<int:pk>/', views.ExtractedDataDeleteView.as_view(), name='extracted_data_delete'),
]

from .views import StageTrackingListView,StageTrackingDetailView,OrganizationsInStageView

urlpatterns=[
    path("stagetracking",StageTrackingListView.as_view(),name="stage-tracking-list"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stage-tracking-detail"),
    path("organizations-in-stage/<str:stage_name>/", OrganizationsInStageView.as_view(), name="organizations-in-stage"),


 
]
