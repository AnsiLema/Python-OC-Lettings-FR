from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Represents a user profile associated with a single user account.

    This class is an extension of the User model, allowing for additional
    information related to a user, such as their favorite city. It utilizes a
    one-to-one relationship with the User model to store supplementary user data.

    :ivar user: The associated user account. It is a one-to-one relationship with
        the User model.
    :ivar favorite_city: The user's favorite city, stored as a string with a
        maximum length of 64 characters. This field is optional.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_new')
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name = 'profile'

    def __str__(self):
        return self.user.username
