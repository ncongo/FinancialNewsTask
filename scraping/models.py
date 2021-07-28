from django.db import models

# Create your models here.
class News(models.Model):
	description = models.CharField(max_length=8000)
	guid = models.CharField(max_length=100)
	link = models.CharField(max_length=255)
	pubDate = models.DateField()
	title = models.CharField(max_length=255)