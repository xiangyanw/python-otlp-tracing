from django.test import TestCase
from django.urls import reverse


class FrontendTests(TestCase):
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the polls index.")
        
    def test_get_user_info_success(self):
        url = reverse('get_user_info', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User Information")  
        self.assertContains(response, "Username: testuser")
        self.assertContains(response, "Email: test@example.com")
        
    def test_get_user_info_failure(self):
        url = reverse('get_user_info', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 500)

