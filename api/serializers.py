from rest_framework import serializers
from .models import User, Book, BlackListedToken


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class BookSerializer(serializers.ModelSerializer):
	seller_username = serializers.SerializerMethodField('get_seller_username')

	def get_seller_username(self, book):
		#print(book, book["seller"])
		return book.seller.username

	class Meta:
		model = Book
		fields = '__all__'

class BlackListedTokenSerializer(serializers.ModelSerializer):
	class Meta:
		model = BlackListedToken
		fields = '__all__'