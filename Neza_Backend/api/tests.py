from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user_registration.models import UserProfile 
from .serializers import UserProfileSerializer
from rest_framework.authtoken.models import Token 


class UserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_users(self):
        UserProfile.objects.create(username="user1", email="user1@example.com")
        UserProfile.objects.create(username="user2", email="user2@example.com")

        url = reverse('user_list_view')

        response = self.client.get(url)
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        url = reverse('user_list_view')
        data = {'username': 'new_user', 'email': 'new_user@example.com', 'password': 'password'}

        response = self.client.post(url, data, format='json')


class UserDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserProfile.objects.create_user(username="test_user", email="test@example.com", password="testpassword")
        self.token, _ = Token.objects.get_or_create(user=self.user)

    def test_get_user(self):
        url = reverse('user_detail_view')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get(url)
        serializer = UserProfileSerializer(self.user)
        self.assertEqual(response.data, serializer.data)

    def test_update_user(self):
        url = reverse('user_detail_view')

        self.client.force_authenticate(user=self.user)
        data = {'username': 'updated_user'}

        response = self.client.put(url, data, format='json')

        self.user.refresh_from_db()

    def test_delete_user(self):
        url = reverse('user_detail_view')

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(url)
        self.assertEqual(UserProfile.objects.count(), 0)

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
