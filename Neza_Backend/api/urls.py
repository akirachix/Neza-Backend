from django.urls import path
from .views import StageTrackingListView,StageTrackingDetailView,OrganizationsInStageView

urlpatterns=[
    path("stagetracking",StageTrackingListView.as_view(),name="stage-tracking-list"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stage-tracking-detail"),
    path("organizations-in-stage/<str:stage_name>/", OrganizationsInStageView.as_view(), name="organizations-in-stage"),


 
]