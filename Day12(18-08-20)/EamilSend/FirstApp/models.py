from django.db import models

# Create your models here.

class Email(models.Model):
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	Email=models.EmailField(max_length=50)
	
	img=models.ImageField(upload_to='attachments/',null=True)

	username=models.CharField(max_length=50,null=True)
	password=models.CharField(max_length=20)
