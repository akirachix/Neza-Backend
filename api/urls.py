from django.urls import path
from . import views
from .views import OrganizationsInStageView, StageTrackingListView, StageTrackingDetailView, UserDetailView, UserView, login, logout, DashboardListView, ProfileImageView, LocationListCreateView, LocationDetailView


urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path("extracted_data/", views.ExtractedDataListView.as_view(),name="extracted_data_list_view"),
    path('extracted_data/<int:pk>/', views.ExtractedDataDetailView.as_view(), name='extracted_data_detail'),
    path('extracted_data/delete/<int:pk>/', views.ExtractedDataDeleteView.as_view(), name='extracted_data_delete'),
    path('users/', UserView.as_view(), name = 'user_list_view'),
    path('user/details/', UserDetailView.as_view(), name='user_detail_view'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path("dashboard_location_details/", DashboardListView.as_view(),name="dashboard_list_view"),
    path("stagetracking",StageTrackingListView.as_view(),name="stage-tracking-list"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stage-tracking-detail"),
    path("organizations-in-stage/<str:stage_name>/", OrganizationsInStageView.as_view(), name="organizations-in-stage"),
    path('user/image/', ProfileImageView.as_view(), name='profile_image_view'),
    path('locations/', LocationListCreateView.as_view(), name='location_list_create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    
]



