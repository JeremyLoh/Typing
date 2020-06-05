from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts')

    def get_absolute_url(self):
        # To find location to specific post
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
