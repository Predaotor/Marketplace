from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Item, Category
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from core.views import index, contact, signup, login_view, logout_view
from core.forms import SignupForm, LoginForm

# Create Test class for core views

class TestViews(TestCase):
    # Set up the client and urls
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('core:index')
        self.contact_url = reverse('core:contact')
        self.signup_url = reverse('core:signup')
        self.login_url = reverse('core:login')
        self.logout_url = reverse('core:index')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        
    # Test views for index, contact, signup, login
    def test_index(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/index.html')
        
    def test_contact(self):
        response=self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/contact.html')
        
    def test_signup(self):
        response=self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/signup.html')
        
    def test_login(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/login.html')
        
  
        
