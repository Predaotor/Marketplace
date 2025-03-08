from django.test import TestCase 
from conversation.models import Conversation, ConversationMessage
from item.models import Item, Category
from django.contrib.auth.models import User



class ConversationModelTestCase(TestCase):
    def setUp(self):
        self.category=Category.objects.create(name='Test Category')
        self.user1=User.objects.create_user(username='user1', password='password')
        self.user2=User.objects.create_user(username='user2', password='password')
        self.item=Item.objects.create(category=self.category, name='item', description='description', price=10, created_by=self.user1)
        self.conversation=Conversation.objects.create(item=self.item)
        self.conversation.members.add(self.user1)
        self.conversation.members.add(self.user2)
        self.conversation.save()
        self.message1=ConversationMessage.objects.create(conversation=self.conversation, content='message1', created_by=self.user1)
        self.message2=ConversationMessage.objects.create(conversation=self.conversation, content='message2', created_by=self.user2)
        
    def test_conversation(self):
        self.assertEqual(self.conversation.item, self.item)
        self.assertEqual(self.conversation.members.count(), 2)
        self.assertEqual(self.conversation.members.first(), self.user1)
        self.assertEqual(self.conversation.members.last(), self.user2)
        self.assertEqual(self.conversation.messages.count(), 2)
        self.assertEqual(self.conversation.messages.first(), self.message1)
        self.assertEqual(self.conversation.messages.last(), self.message2)
        