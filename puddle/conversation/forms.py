from django import forms 

from .models import ConversationMessage 

"""
Create a form to allow users to send messages in a conversation
"""

class ConversationMessageForm(forms.ModelForm):
    class Meta: 
        model=ConversationMessage 
        fields=('content',)
        widgets= {
            'content':forms.Textarea(attrs={
                'class':'w-full py-4  px-6 rounded-xl border'                   
        }) }