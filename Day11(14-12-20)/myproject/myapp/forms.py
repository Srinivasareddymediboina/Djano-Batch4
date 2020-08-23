from django import forms
from .models import Library

class LibraryForm(forms.Form):
	branches = (
			('ece','ECE'),
			('cse','CSE'),
			('it','IT'),
			('mech','MECH'),
			('civil','CIVIL'),
			('chem','CHEM')
		)
	book_number = forms.IntegerField()
	book_name = forms.CharField(max_length=50)
	author = forms.CharField(max_length=30)
	department = forms.ChoiceField(choices = branches)
	publication_Date = forms.DateField()

	class Meta:
		model = Library
		fields = '__all__'

