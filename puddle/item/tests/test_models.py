from django.test import TestCase 
from item.models import Category, Item
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage
from django.conf import settings
import os

# Test the Category and Item models

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category=Category.objects.create(name='Test Category')
    
    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')
        
class ItemTestCase(TestCase):
    def setUp(self):
        self.category=Category.objects.create(name='Test Category')
        self.user=User.objects.create_user(username='testuser', password='testpassword')
        self.item=Item.objects.create(category=self.category, name='Test Item', description='Test Description', price=10.00, created_by=self.user)
    
    def test_item_str(self):
        self.assertEqual(str(self.item), 'Test Item')
        
    def test_image_upload(self):
        # Create a test image file
        image_path=os.path.join(settings.BASE_DIR, 'item/tests/car.webp')
        with open(image_path, 'rb') as image:
            image_file=SimpleUploadedFile('test_image.jpg', image.read())
            
        # Assign the image file to the item
        self.item.image=image_file
        self.item.save()
        
        # Check that the image file was saved to the correct location
        self.assertTrue(default_storage.exists(self.item.image.name))
        
    def tearDown(self):
        if self.item.image and  default_storage.exists(self.item.image.name):
            default_storage.delete(self.item.image.name)
        self.item.delete()
        self.user.delete()
        self.category.delete()