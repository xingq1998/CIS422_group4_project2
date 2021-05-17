from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return HttpResponse("Hello, world. You're at the user index.")


def my_signup(request):
    if request.user.is_authenticated:
        return render(request, 'user/signup.html', None)
    if request.method == 'POST':
        post_dict = request.POST
        username = post_dict.get("username", "")
        email = post_dict.get("email", "")
        password = post_dict.get("password", "")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return render(request, 'user/login.html', None)
    else:
        return render(request, 'user/signup.html', None)


def my_login(request):
    if request.method == 'POST':
        post_dict = request.POST
        username = post_dict.get("username", "")
        password = post_dict.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html')
    else:
        return render(request, 'user/login.html')


def my_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'user/logout.html')