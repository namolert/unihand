from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.hashers import check_password

from users.forms import RegisterForm, LoginForm
from users.models import User
from users.permissions import is_student, is_professor, is_admin


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def role_based_redirect(request):
    if request.user.role == "Student":
        return redirect("student_home")
    elif request.user.role == "Professor":
        return redirect("professor_home")
    elif request.user.role == "Admin":
        return redirect("admin_home")
    else:
        return redirect("home")

def student_home(request):
    is_student(request.user)
    return render(request, "main/student/home.html")

def professor_home(request):
    is_professor(request.user)
    return render(request, "main/professor/home.html")

def admin_home(request):
    is_admin(request.user)
    return render(request, "main/admin/home.html")