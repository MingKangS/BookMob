from django.shortcuts import render
from rest_framework import generics, status
from ..serializers import UserSerializer, BookSerializer
from ..models import User, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import json

# Create your views here.

class ListAllBooksView(APIView):
	serializer_class = BookSerializer

	def get(self, request, format=None):
		query_set = Book.objects.all()
		
		book_list = self.serializer_class(query_set, many=True)
		return Response({'book_list': book_list.data}, status=status.HTTP_200_OK)

class AddBookView(APIView):
	serializer_class = BookSerializer

	def post(self, request, format=None):
		#serializer = self.serializer_class(data=request.data)
		#if serializer.is_valid():
		try:
			title = request.data['title']
			author = request.data['author']
			date_posted = request.data['date_posted']
			#user = User.objects.filter(id=payload['id']).first()
			seller = User.objects.filter(id=request.data['seller']).first()
			print("test", seller)
			description = request.data['description']
			condition = request.data['condition']
			price = request.data['price']

			book = Book(title=title, author=author, date_posted=date_posted, seller=seller,
					description=description, condition=condition, price=price)
			print("test", seller)
			book.save()
			print("test", seller)
			return Response(status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({"BAD_REQUEST": e.message}, status=status.HTTP_400_BAD_REQUEST)
