from django.test import TestCase
from django.contrib.auth.models import AbstractUser
from user_authentication.models import UserProfile


class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = UserProfile.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsNotNone(self.user.date_created)
        self.assertIsNotNone(self.user.date_updated)

    def test_user_profile_str(self):
        self.assertEqual(str(self.user),'testuser')

