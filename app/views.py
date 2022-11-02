from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

# Create your views here.

# create a viewset
# modelviewset creates view according to models and would have all 
# required get, post, etc.. methods with minimal code to write
class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	# specify serializer to be used
	serializer_class = BookSerializer

class BookAPIView(APIView):
	"""
	List all Books or Create a new Book
	"""
	def get(self, request, format=None):
		books = Book.objects.all()	
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)