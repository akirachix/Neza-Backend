from django.urls import path
from .views import StageTrackingListView,StageTrackingDetailView

urlpatterns=[
    path("stagetracking",StageTrackingListView.as_view(),name="stage-tracking-list"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stage-tracking-detail"),
   
 
]