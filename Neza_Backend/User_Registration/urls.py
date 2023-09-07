from django.urls import path
from .views import register_user
urlpatterns = [
    path('user/register/', register_user, name='register_user'),
]