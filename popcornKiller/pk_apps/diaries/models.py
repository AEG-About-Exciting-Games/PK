import os

from django.core.files.storage import FileSystemStorage
from django.db import models

from pk_apps.accounts.models import User
from popcornKiller.settings import BASE_DIR


fs = FileSystemStorage(location=os.path.join(BASE_DIR, 'media'))

class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diaries')
    movie = models.CharField(max_length=100, null=True, blank=True)
    cinema = models.CharField(max_length=255, null=True, blank=True)
    loc_x = models.DecimalField(max_digits=8, decimal_places=4)
    loc_y = models.DecimalField(max_digits=8, decimal_places=4)
    photo = models.ImageField(upload_to='photos/', storage=fs, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.writer}: {self.title} - {self.movie}"
