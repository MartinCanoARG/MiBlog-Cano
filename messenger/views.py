from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messenger/inbox.html', {'messages': messages})

@login_required
def outbox(request):
    messages = Message.objects.filter(sender=request.user).order_by('-timestamp')
    return render(request, 'messenger/outbox.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            return redirect('messenger:outbox')
    else:
        form = MessageForm()
    return render(request, 'messenger/send_message.html', {'form': form})

@login_required
def view_message(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    if msg.receiver == request.user:
        msg.is_read = True
        msg.save()
    return render(request, 'messenger/view_message.html', {'message': msg})
