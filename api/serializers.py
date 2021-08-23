from rest_framework import serializers
from .models import User, Book


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('title', 'author', 'date_posted', 'seller')