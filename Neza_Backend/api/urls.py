from django.urls import path
from .views import StageTrackingListView,StageTrackingDetailView

urlpatterns=[
    path("stagetracking",StageTrackingListView.as_view(),name="stagetracking_list_view"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stragetracking_detail_view"),
   
 
]