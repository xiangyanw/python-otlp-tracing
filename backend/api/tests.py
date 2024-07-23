from django.test import TestCase
from django.urls import reverse

from .models import User


class UserTests(TestCase):
    def setUp(self):
        User.objects.create(username='testuser', email='test@example.com')
        
    def test_user_info_valid_user_id(self):
        user = User.objects.get(username='testuser')
        url = reverse('get_user_info', args=[user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'username': 'testuser',
            'email': 'test@example.com'
        })
        
    def test_user_info_invalid_user_id(self):
        url = reverse('get_user_info', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'User not found'})
