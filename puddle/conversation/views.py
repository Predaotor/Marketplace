from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required
from item.models import Item

# Path: puddle/conversation/views.py
# Create function to create new conversations
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, id=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations.exists():
        return redirect('conversation:inbox', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # create a new conversation and save to database
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            # create a new conversation message and save to database
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })

# create function to view conversations
@login_required 
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })


# create function to view conversation details and text back 
@login_required 
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members__in=[request.user.id])
    if request.method=="POST":

        # create a new conversation message and save to database
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detail', pk=pk) 

    else:
        form = ConversationMessageForm()
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })

