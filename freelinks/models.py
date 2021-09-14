from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    """This is the main user profile for the user that will have the main user details"""
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)


class LinkCollection(models.Model):
    """A user can have different link templates that can be activated at anytime"""
    pass


class Link(models.Model):
    """This will be a list of all the links for the user"""
    pass
