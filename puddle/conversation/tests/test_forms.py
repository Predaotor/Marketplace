from django.test import TestCase
from conversation.forms import ConversationMessageForm 
from conversation.models import ConversationMessage, Conversation
from item.models import Item, Category
from django.contrib.auth.models import User
import time

class ConversationTestForms(TestCase):
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
        
    def test_conversation_message_form(self):
        form_data={'content':'message3'}
        form=ConversationMessageForm(data=form_data)
        self.assertTrue(form.is_valid())
        message=form.save(commit=False)
        message.conversation=self.conversation
        message.created_by=self.user1
        message.save()
        self.assertEqual(self.conversation.messages.count(), 3)
        self.assertEqual(self.conversation.messages.last(), message)
        self.assertEqual(self.conversation.messages.last().content, 'message3')
        self.assertEqual(self.conversation.messages.last().created_by, self.user1)
        self.assertEqual(self.conversation.messages.last().conversation, self.conversation)