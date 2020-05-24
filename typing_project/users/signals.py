from django.db.models.signals import post_save
# User model is the sender: sending signal
from django.contrib.auth.models import User
# Receiver: function that obtains signal and performs a task
from django.dispatch import receiver

from .models import Profile

# When sender (User) is saved, send signal (post_save)
# create_profile function is the receiver that accepts arguments
# obtained from signal (post_save)
# **kwargs is used to accept any additional arguments provided to function


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Create a Profile for each new User
    if created:
        Profile.objects.create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    # When User is saved, save their Profile as well
    instance.profile.save()
