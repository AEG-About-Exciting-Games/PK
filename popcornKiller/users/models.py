from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
