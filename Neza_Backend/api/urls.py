from django.urls import path
<<<<<<< HEAD
from .views import StageTrackingListView,StageTrackingDetailView,OrganizationsInStageView

urlpatterns=[
    path("stagetracking",StageTrackingListView.as_view(),name="stage-tracking-list"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stage-tracking-detail"),
    path("organizations-in-stage/<str:stage_name>/", OrganizationsInStageView.as_view(), name="organizations-in-stage"),


 
=======
from .views import DashboardListView


app_name = 'api'
urlpatterns=[
    path("dashboard_location_details/", DashboardListView.as_view(),name="dashboard_list_view"),
>>>>>>> 931406d46d7896fb6062b2246a3ab0a3bfdd150f
]