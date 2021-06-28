from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user('tbello','tbello@gmail.com', '123password@')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'tbello@gmail.com')
        
    def test_creates_super_user(self):
        user = User.objects.create_superuser('tbello','tbello@gmail.com', '123password@')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'tbello@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",email ='tbello@gmail.com', password='123password@')
        self.assertRaisesMessage(ValueError, 'The given username must be set')
     
    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='',email='tbello@gmail.com', password='123password@')

