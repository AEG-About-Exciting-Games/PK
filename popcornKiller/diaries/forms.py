from django import forms
from .models import Diary


class DiariesForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'content', 'movie']
