from email import header
import json
from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="tu1", password='tp1', 
                            email='te1', first_name='tf1',
                            last_name='tl1')

    def test_user_token(self):
        """Get token is correct"""
        c = Client()
        dat={
            "username": "tu1",
            "password": "tp1"
            }
        
        response =c.post('/api/auth/token',dat, content_type='application/json')
        data=response.json()
        self.assertEqual(data['token_type'], "bearer")
        self.assertEqual(response.status_code, 200)