from django.db import models

# Create your models here.

class Movies(models.Model):
	moviename=models.CharField(max_length=50)
	hero=models.CharField(max_length=50)
	heroin=models.CharField(max_length=50)
	director=models.CharField(max_length=50)
	poster=models.ImageField(upload_to='poster/',null=True)
	password=models.CharField(max_length=50)
	
