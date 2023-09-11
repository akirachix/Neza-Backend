from django.test import TestCase
from django.contrib.auth.models import User
from user_registration.models import UserProfile


class UserProfileModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

        self.user_profile = UserProfile.objects.create(
            user=self.user,
            email='test@example.com'
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.email, "test@example.com")
        self.assertIsNotNone(self.user_profile.date_created)
        self.assertIsNotNone(self.user_profile.date_updated)

    def test_user_profile_str(self):
        self.assertEqual(str(self.user_profile),'testuser')

