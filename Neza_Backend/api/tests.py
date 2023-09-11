from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user_registration.models import User
from .serializers import UserSerializer
from user_registration.models import UserProfile
from rest_framework.authtoken.models import Token

class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_users(self):
        User.objects.create(username="user1", email="user1@example.com")
        User.objects.create(username="user2", email="user2@example.com")

        url = reverse('user_list_view')  

        response = self.client.get(url)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        url = reverse('user_list_view')  
        data = {'username': 'new_user', 'email': 'new_user@example.com', 'password':'password'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'new_user')

class UserDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="test_user", email="test@example.com", password="testpassword")
        self.token, _ = Token.objects.get_or_create(user=self.user)

    def test_get_user(self):
        url = reverse('user_detail_view')  
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get(url)
        serializer = UserSerializer(self.user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_user(self):
        url = reverse('user_detail_view')  

        self.client.force_authenticate(user=self.user)
        data = {'username': 'updated_user'}

        response = self.client.put(url, data, format='json')
        print(response.content)
        self.user.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.user.name, 'test_user')

    def test_delete_user(self):
        url = reverse('user_detail_view')  

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_user_login(self):
        url = reverse('login')

        data = {
            'username': 'test_user',
            'password': 'testpassword'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)


    def test_user_logout(self):
        url = reverse('logout')

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

