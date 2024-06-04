from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

from .models import User
from .forms import UserForm


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        user = User(name=name, email=email, password=password)
        user.save()
        return redirect('/rest-auth/registration/')
    else:
        return render(request, 'register_view.html')


def login(request):
    if request.method == "POST":
        
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, 'login_view.html', context)
