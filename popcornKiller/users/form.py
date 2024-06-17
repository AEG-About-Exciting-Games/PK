from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('email', 'nickname', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
