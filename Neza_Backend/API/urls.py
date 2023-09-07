from django.urls import path
from .views import UserDetailView
from .views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name = 'user_list_view'),
    path('user/<int:id>', UserDetailView.as_view(), name='user_detail_view')
]