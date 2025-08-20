from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

"""
- view for user registration.
- uses Django REST Framework's CreateAPIView to handle POST requests for creating new users.
"""
class RegisterView(generics.CreateAPIView):
	queryset = User.objects.all()  # retrieves all user records from the database
	serializer_class = UserRegisterSerializer  # serializer used for validating and creating user instances
