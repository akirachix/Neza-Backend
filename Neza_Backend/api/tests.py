from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from User_Registration.models import User
from .serializers import UserSerializer

class UserListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_users(self):
        User.objects.create(name="user1", email="user1@example.com")
        User.objects.create(name="user2", email="user2@example.com")

        url = reverse('user_list_view')  

        response = self.client.get(url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        url = reverse('user_list_view')  
        data = {'username': 'new_user', 'email': 'new_user@example.com'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'new_user')

class UserDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name="test_user", email="test@example.com")

    def test_get_user(self):
        url = reverse('user_detail_view', args=[self.user.id])  

        response = self.client.get(url)
        serializer = UserSerializer(self.user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_user(self):
        url = reverse('user_detail_view', args=[self.user.id])  
        data = {'username': 'updated_user'}

        response = self.client.put(url, data, format='json')
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.user.name, 'test_user')

    def test_delete_user(self):
        url = reverse('user_detail_view', args=[self.user.id])  

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)


