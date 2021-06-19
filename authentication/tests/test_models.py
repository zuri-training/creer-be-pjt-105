from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user('tbello','tbello@gmail.com', '123password@')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'tbello@gmail.com')
        
    def test_creates_user(self):
        user = User.objects.create_user('tbello','tbello@gmail.com', '123password@')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'tbello@gmail.com')