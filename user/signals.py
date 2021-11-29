from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from user.models import UserProfile


@receiver(post_save, sender=User)
def user_post_save_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)