from django.db import models
from django.contrib.auth.models import User, AbstractUser



class UserProfile(models.Model):
    """User profile model implementation"""


    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='user',
        related_name='profile',
    )


    birthday = models.DateField(
        null=True,
        blank=True,


    )
    img = models.ImageField(blank=True,null=True, upload_to="profile/")

    myself_info = models.TextField(null=True,blank=True, default=None)

    def __repr__(self):
        """Return a string representation of an instance"""

        return f"<UserProfile ('{self}')>"

    def __str__(self):
        """Return a string version of an instance"""

        return self.user.__str__()