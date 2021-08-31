from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(null=False ,max_length=20, unique=True)
	email = models.EmailField(null=False ,max_length=50, unique=True)
	password = models.CharField(null=False, max_length=50)
	contact = models.CharField(null=False, max_length=30)

class Book(models.Model):
	title = models.CharField(null=False ,max_length=40)
	author = models.CharField(null=False ,max_length=40)
	date_posted = models.DateField(null=False)
	seller = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
	description = models.TextField(null=False, max_length=200)
	condition = models.PositiveSmallIntegerField(null=False)
	price = models.DecimalField(null=False, max_digits=7, decimal_places=2)

class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)

