from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=10)
    writer = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name='post_writer')
    movie = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
