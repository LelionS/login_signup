# accounts/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def login_signup(request):
    if request.method == 'POST':
        # Handle login
        if 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to your desired page
            else:
                messages.error(request, 'Invalid username or password')

        # Handle signup
        elif 'signup' in request.POST:
            username = request.POST['new_username']
            password = request.POST['new_password']
            email = request.POST['email']
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages.success(request, 'Account created successfully! You can now log in.')
                return redirect('login_signup')

    return render(request, 'accounts/login_signup.html')
