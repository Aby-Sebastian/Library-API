from rest_framework import serializers
from .models import Book, BookImages


class BookImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookImages
		fields = ('id', 'book', 'image')

class BookSerializer(serializers.ModelSerializer):
	image = BookImageSerializer(many=True)
	class Meta:
		model = Book
		fields = ['id', 'title', 'description', 'image']
