from django.db import models

# Create your models here.

class Library(models.Model):
	branches = (
			('ece','ECE'),
			('cse','CSE'),
			('it','IT'),
			('mech','MECH'),
			('civil','CIVIL'),
			('chem','CHEM')
		)
	Book_Number = models.IntegerField()
	Book_Name = models.CharField(max_length=50)
	Author = models.CharField(max_length=30)
	Department = models.CharField(max_length=20,choices = branches)
	Publication_Date = models.CharField(max_length=30)

	def __str__(self):
		return self.Book_Name + self.Author