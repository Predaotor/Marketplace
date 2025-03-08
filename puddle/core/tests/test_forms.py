from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Item, Category
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from core.views import index, contact, signup, login_view, logout_view
from core.forms import SignupForm, LoginForm

class TestForms(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='testuser', password='testpassword')
        self.category=Category.objects.create(name='Test Category')
        
        
    def test_signup_form_valid_data(self):
        form=SignupForm(data={
            'username':'testuser4',
            'email':'test123@mail.ru',
            'password1':'testpassword',
            'password2':'testpassword' })
        print(form.errors)
        self.assertTrue(form.is_valid())
        
        
    def test_signup_form_no_data(self):
        form=SignupForm(data={})
        self.assertFalse(form.is_valid())   
        self.assertEquals(len(form.errors), 4)
        
    def test_login_form_valid_data(self):
        form=LoginForm(data={
            'username':'testuser',
            'password':'testpassword'})
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)
        