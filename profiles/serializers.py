from rest_framework import serializers
from .models import Author
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Author
        fields = "__all__"

