from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(null=False ,max_length=20, unique=True)
    email = models.EmailField(null=False ,max_length=50, unique=True)
    password = models.CharField(null=False, max_length=50)
