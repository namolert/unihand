from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

from users.forms import RegisterForm
from users.models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})