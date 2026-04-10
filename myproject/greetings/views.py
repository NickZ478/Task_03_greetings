from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NameForm
from .models import UserName

def index(request):
    greeting_message = None
    form = NameForm()
    
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            user_name = form.save()
            greeting_message = f"Здравствуйте, {user_name.name}!"
            messages.success(request, greeting_message)
            form = NameForm()
        else:
            if 'name' in form.errors:
                messages.error(request, form.errors['name'][0])
    
    all_names = UserName.objects.all().order_by('-created_at')[:10]
    
    context = {
        'form': form,
        'greeting_message': greeting_message,
        'all_names': all_names,
    }
    
    return render(request, 'greetings/index.html', context)
