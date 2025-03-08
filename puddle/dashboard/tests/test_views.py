from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from item.models import Item, Category
from django.test import Client
import os 
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

# Create Test class for dashboard views

class TestDashboardForm(TestCase):
    def setUp(self):
        self.client=Client() 
        self.user=User.objects.create_user(username="testuser2", password="testpassword")
        self.category=Category.objects.create(name="testcategory")
        
        self.item1=Item.objects.create(
            category=self.category,
            name='Test Item1',
            description='Test Description',
            price=10.00,
            created_by=self.user
        )
        self.item2=Item.objects.create(
            category=self.category,
            name='Test Item2',
            description='Test Description',
            price=10.00,
            created_by=self.user
        )
        image_path=os.path.join(settings.BASE_DIR, 'dashboard/tests/OIP.webp')
        with open(image_path, 'rb') as image:
            image_file=SimpleUploadedFile('test_image.webp', image.read())
            
        # Assign the image file to the item
        self.item1.image=image_file
        self.item1.save()
        self.item2.image=image_file
        self.item2.save()
        self.url=reverse('dashboard:index')
        
    def test_redirect_if_not_logged_in(self):
        """Ensure unauthenticated users are redirected to the login page."""
        response=self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))
        
    def test_authenticted_user_sees_Their_Items(self):
        """Ensure authenticated users see their items."""
        self.client.login(username='testuser2', password='testpassword')
        response=self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Item1')
        self.assertContains(response, 'Test Item2')
        