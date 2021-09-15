from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Profile(models.Model):
    """This is the main user profile for the user that will have the main user details"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user}--{self.first_name} {self.last_name}"


class LinkProject(models.Model):
    """A user can have different link projects that can be activated at anytime"""
    project_name = models.CharField(max_length=20, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse('projects', kwargs={'slug': self.slug})


class Link(models.Model):
    """This will be a list of all the links for the user"""
    name = models.CharField(max_length=20, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    project = models.ForeignKey(LinkProject, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
