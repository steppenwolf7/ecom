from django.db import models
from django.contrib.auth.models import User
from index.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Sortowanie postów od najnowszego do najstarszego

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"   