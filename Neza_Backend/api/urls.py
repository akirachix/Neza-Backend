from django.urls import path
from .views import UserView,UserDetailView
from .views import login, logout
from .views import DashboardListView

app_name = 'api'

urlpatterns = [
    path('users/', UserView.as_view(), name = 'user_list_view'),
    path('user/details/', UserDetailView.as_view(), name='user_detail_view'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path("dashboard_location_details/", DashboardListView.as_view(),name="dashboard_list_view"),


]