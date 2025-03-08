from django.test import TestCase 
from conversation.views import new_conversation, delete_message, inbox, detail
from django.test import Client
from django.urls import reverse
from conversation.models import Conversation, ConversationMessage
from item.models import Item, Category
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage

class ConversationViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='Test Category')
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.item = Item.objects.create(category=self.category, name='item', description='description', price=10, created_by=self.user1)
        self.client.login(username='user1', password='password')
        
    def test_new_conversation(self):
        response = self.client.get(reverse('conversation:new', args=[self.item.id]))
        self.assertEqual(response.status_code, 302)
        
    def test_delete_message(self):
        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user1)
        conversation.members.add(self.user2)
        conversation.save()
        message = ConversationMessage.objects.create(conversation=conversation, content='message', created_by=self.user1)
        response = self.client.get(reverse('conversation:delete', args=[message.id]))
        self.assertEqual(response.status_code, 302)
        
    def test_inbox(self):
        response = self.client.get(reverse('conversation:inbox')) 
        self.assertEqual(response.status_code, 200)
        
    def test_detail(self):
        conversation = Conversation.objects.create(item=self.item)
        conversation.members.add(self.user1)
        conversation.members.add(self.user2)
        conversation.save() 
        response = self.client.get(reverse('conversation:detail', args=[conversation.id]))
        self.assertEqual(response.status_code, 200)
        