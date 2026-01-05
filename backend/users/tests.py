from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(APITestCase):
    def test_registration(self):
        url = reverse('auth_register')
        data = {'email': 'test@example.com', 'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'test@example.com')

    def test_login(self):
        email = 'test@example.com'
        password = 'password123'
        User.objects.create_user(username='testuser', email=email, password=password)
        
        url = reverse('auth_login')
        data = {'email': email, 'password': password}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
