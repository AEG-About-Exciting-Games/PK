from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, LoginForm, UserUpdateForm


def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('box_office:daily_view')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('box_office:daily_view')

        else:
            render(request, 'accounts/login.html', {'form': form, 'error': 'Invalid email or password'})

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('accounts:login')


@login_required
def update_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:update')

    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update.html', {'form': form})


@login_required
def unsubscribe_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect('accounts.login')
    return render(request, 'accounts/unsubscribe.html')
