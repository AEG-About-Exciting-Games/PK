from django import forms

from .models import Diary


class DiariesForm(forms.ModelForm):
    movie = forms.CharField(
        widget=forms.TextInput(attrs={'readonly':'readonly'})
    )

    class Meta:
        model = Diary
        fields = ['title', 'content', 'movie', 'photo']
