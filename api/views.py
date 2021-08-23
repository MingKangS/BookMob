from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

class SignUpView(APIView):
	serializer_class = UserSerializer

	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		#print(request.data["username"], request.data["password"])
		if serializer.is_valid():
			username = serializer.data.get('username')
			email = serializer.data.get('email')
			password = serializer.data.get('password')
			queryset_username, queryset_email = User.objects.filter(username=username), User.objects.filter(email=email)
			print(queryset_username,queryset_email,queryset_username.exists())
			if queryset_username.exists() or queryset_email.exists():
				cred = "username" if queryset_username.exists() else "email"
				err_message = "Invalid credentials. This " + cred + " already exist."
				return Response({'Bad Request': err_message}, status=status.HTTP_400_BAD_REQUEST)
			user = User(username=username, email=email, password=password)
			user.save()
			if not self.request.session.exists(self.request.session.session_key):
				self.request.session.create()
			return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

		return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class LogInView(APIView):
	serializer_class = UserSerializer

	def post(self, request, format=None):
		username = request.data["username"]
		password = request.data["password"]
		
		queryset = User.objects.filter(username=username)
		if queryset.exists():
			user = queryset[0]
			print(user,user.password)
			if user.password == password:
				if not self.request.session.exists(self.request.session.session_key):
					self.request.session.create()
				return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
			return Response({'Bad Request': 'The password entered is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'Bad Request': 'The username entered is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)