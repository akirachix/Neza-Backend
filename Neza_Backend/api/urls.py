from django.urls import path
from .views import UserView,UserDetailView
from .views import user_login, user_logout

urlpatterns = [
    path('users/', UserView.as_view(), name = 'user_list_view'),
    path('user/details/', UserDetailView.as_view(), name='user_detail_view'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]