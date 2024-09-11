from django.db import models
from accounts.models import User


class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diaries')
    movie = models.CharField(max_length=100, null=True, blank=True)
    cinema = models.CharField(max_length=255, null=True, blank=True)
    loc_x = models.DecimalField(max_digits=4, decimal_places=4, default=33.4507)
    loc_y = models.DecimalField(max_digits=4, decimal_places=4, default=126.5706)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.writer}: {self.title} - {self.movie}"
