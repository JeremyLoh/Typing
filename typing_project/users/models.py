from django.db import models
from django.contrib.auth.models import User
from PIL import Image


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

    def save(self):
        # Override save method for Profile model
        super().save()
        # Use pillow library to resize image
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
