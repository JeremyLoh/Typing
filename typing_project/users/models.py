from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # one to one relationship with existing User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # upload_to is the directory that images get uploaded to
    image = models.ImageField(default='default.svg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    @property
    def has_bio(self):
        # Check if bio is empty
        return self.bio is not None and self.bio.strip() != ''

    def __str__(self):
        return f"{self.user.username} Profile"
