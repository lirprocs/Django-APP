from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        nickname = request.POST['nickname']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=nickname).exists():
            messages.error(request, 'Nickname is already taken.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already taken.')
            return redirect('register')

        user = User.objects.create_user(nickname, email, password)
        user.save()

        user = authenticate(request, username=nickname, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'users/register.html')


def login_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(1209600)  # 2 weeks
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'users/login.html')


def log_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')


