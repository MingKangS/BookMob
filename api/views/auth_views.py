from django.shortcuts import render
from rest_framework import generics, status
from ..serializers import UserSerializer, BlackListedTokenSerializer
from ..models import User, BlackListedToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import jwt, datetime
from .utils import create_token
from config import SECRET

# Create your views here.

class SignUpView(APIView):
	serializer_class = UserSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			username = serializer.data.get('username')
			email = serializer.data.get('email')
			password = serializer.data.get('password')
			
			user = User(username=username, email=email, password=password)
			user.save()

			token = create_token(user.id)
			return Response({ "token": token }, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogInView(APIView):
	serializer_class = UserSerializer

	def post(self, request, format=None):
		username = request.data["username"]
		password = request.data["password"]
		
		queryset = User.objects.filter(username=username)
		if queryset.exists():
			user = queryset[0]
			if user.password == password:
				token = create_token(user.id)
				return Response({ "token": token }, status=status.HTTP_200_OK)
			return Response({'Bad Request': 'The password entered is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'Bad Request': 'The username entered is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

class getAuthenticatedUser(APIView):
	def get(self, request, token, format=None):
		try:
			payload = jwt.decode(token, SECRET, algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			return Response({'UNAUTHORIZED': 'You are not logged in.'}, status=status.HTTP_401_UNAUTHORIZED)

		try:
			is_blackListed = BlackListedToken.objects.get(token=token)
			if is_blackListed:
				return Response({'UNAUTHORIZED': 'Your token has expired.'}, status=status.HTTP_401_UNAUTHORIZED)
		except BlackListedToken.DoesNotExist:
			pass
		
		user = User.objects.filter(id=payload['id']).first()
		serializer = UserSerializer(user)
		return JsonResponse(serializer.data, status=status.HTTP_200_OK)

class LogOutView(APIView):
	serializer_class = BlackListedToken

	def post(self, request, format=None):
		jwt = request.data["token"]
		black_listed_token = BlackListedToken(token=jwt)
		black_listed_token.save()

		return Response(status=status.HTTP_200_OK)

