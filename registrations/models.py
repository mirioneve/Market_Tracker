from django.db import models

# Create your models here.
class Registration(models.Model):
    """A class to manage user registration info."""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
