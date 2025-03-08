from django.test import TestCase
from item.forms import NewItemform, EditItemform
from item.models import Item, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
import os 
from django.conf import settings 

class TestForms(TestCase):
    """
    TestForms is a TestCase class that tests the forms in the item app.
    
    """
    def setUp(self):
        """
        setUp is a method that is run before each test case.
        
        """
        
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

        self.new_item_form_data={
            'category': self.category.id,
            'name':'test name',
            'description':'test description',
            'price':100,
            'image':self.item.image,
        }
        self.edit_item_form_data={
            'name':'test name',
            'description':'test description',
            'price':100,
            'image':self.item.image,
            'is_sold':False,
        }
        
    def test_new_item_form_valid_data(self):
        """
        test_new_item_form_valid_data tests the NewItemform with valid data.
        
        """
        form=NewItemform(data=self.new_item_form_data)
        self.assertTrue(form.is_valid())
        
    def test_new_item_form_invalid_data(self):
        """
        test_new_item_form_invalid_data tests the NewItemform with invalid data.
        
        """
        form=NewItemform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
        
    def test_edit_item_form_valid_data(self):
        """
        test_edit_item_form_valid_data tests the EditItemform with valid data.
        
        """
        form=EditItemform(data=self.edit_item_form_data)
        self.assertTrue(form.is_valid())
        
    def test_edit_item_form_invalid_data(self):
        """
        test_edit_item_form_invalid_data tests the EditItemform with invalid data.
        
        """
        form=EditItemform(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)