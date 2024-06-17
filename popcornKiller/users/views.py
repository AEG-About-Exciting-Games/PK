from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .form import SignUpForm, LoginForm, UserUpdateForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            return redirect('users:login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
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
            render(request, 'login.html', {'form': form, 'error': 'Invalid email or password'})

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login')


def update_view(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('users:profile')

    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'update.html', {'form': form})


def unsubscribe_view(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect('users.login')
    return render(request, 'unsubscribe.html')
