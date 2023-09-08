from django.urls import path
from .views import DashboardListView, DashboardView


app_name = 'api'
urlpatterns=[
    path("dashboard/", DashboardListView.as_view(),name="dashboard_list_view"),
    path("dashboarddetails/<int:id>/", DashboardView.as_view(),name="dashboard_detail_view"),
]