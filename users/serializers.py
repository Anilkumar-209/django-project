from django.contrib.auth.models import User
from rest_framework import serializers


"""
UserRegisterSerializer:
- serializer for user registration.
- accepts username, email, and password fields.
- ensures password is write-only (not returned in responses).
- creates a new User instance using Django's create_user method for proper password hashing.
"""
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
