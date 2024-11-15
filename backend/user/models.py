from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username            = models.CharField(max_length=100, unique=True, blank=False)
    email               = models.EmailField(max_length=200, unique=True,blank=False)
    password            = models.CharField(max_length=100, blank=False)
    first_name          = models.CharField(max_length=100)
    last_name           = models.CharField(max_length=100)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)
    
    bio                 = models.TextField()
    academic_title      = models.CharField(max_length=200)

    groups              = None
    user_permissions    = None
    last_login          = None
    date_joined         = None