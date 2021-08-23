from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(null=False ,max_length=20, unique=True)
	email = models.EmailField(null=False ,max_length=50, unique=True)
	password = models.CharField(null=False, max_length=50)

class Book(models.Model):
	title = models.CharField(null=False ,max_length=40)
	author = models.CharField(null=False ,max_length=40)
	date_posted = models.DateField(null=False)
	seller = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

