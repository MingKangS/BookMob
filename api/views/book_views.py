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
