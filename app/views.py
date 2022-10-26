from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# Create your views here.

# create a viewset
class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	# specify serializer to be used
	serializer_class = BookSerializer