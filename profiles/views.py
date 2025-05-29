from django.shortcuts import render
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.

class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



