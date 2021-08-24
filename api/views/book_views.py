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
		if not self.request.session.exists(self.request.session.session_key):
			return Response({'Unauthorized': 'User is not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)
		query_set = Book.objects.all()
		res_query_set = json.loads({"book_list" : [self.serializer_class(book) for book in query_set]})    
		return Response(res_query_set, content_type ="application/json", status=status.HTTP_200_OK)
