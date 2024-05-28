from django.db import models

# Create your models here.
class Posts(models.Model):
    # writer = models.ForeignKey()  # account
    movie = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
