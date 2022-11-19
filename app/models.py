from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 250)
	description = models.TextField()
	image = models.ImageField(upload_to='img', default='', blank=True, null=True)

	def __str__(self):
	  return self.title

class BookImages(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images")
	image = models.ImageField(upload_to='img', default="", null=True, blank=True)