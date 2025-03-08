from django.test import TestCase 
from item.views import browse, detail, new, delete, edit 
from item.models import Item, Category
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from django.core.files.uploadedfile import SimpleUploadedFile 
import os 
from django.conf import settings

# Test item views
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Test Category')
        self.item = Item.objects.create(
            category=self.category,
            name='Test Item',
            description='Test Description',
            price=10.00,
            created_by=self.user
        )
         # Create a test image file
        image_path=os.path.join(settings.BASE_DIR, 'item/tests/car.webp')
        with open(image_path, 'rb') as image:
            image_file=SimpleUploadedFile('test_image.jpg', image.read())
            
        # Assign the image file to the item
        self.item.image=image_file
        self.item.save()

    def test_browse(self):
        response = self.client.get(reverse('item:browse'))
        self.assertEqual(response.status_code, 200)
        
    def test_detail(self):
        response = self.client.get(reverse('item:detail', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)
        
    def test_new(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('item:new'))
        self.assertEqual(response.status_code, 200)
        
    def test_delete(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('item:delete', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)
        
    def test_edit(self):
        self.client.login(username='testuser', password='testpassword') 
        response = self.client.get(reverse('item:edit', args=[self.item.id]))
        self.assertEqual(response.status_code, 200)