from django.urls import path
from .views import DashboardListView


app_name = 'api'
urlpatterns=[
    path("dashboard_location_details/", DashboardListView.as_view(),name="dashboard_list_view"),
]