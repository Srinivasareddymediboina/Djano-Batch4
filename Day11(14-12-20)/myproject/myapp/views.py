from django.shortcuts import render
from .forms import LibraryForm
from .models import Library
from django.http import HttpResponse
# Create your views here.
def addBook(request):
	form = LibraryForm()
	if request.method=='POST':
		form = LibraryForm(request.POST)
		if form.is_valid():
			print(form.data)
			print(form.cleaned_data)
			name = form.data['book_name']
			number = form.data['book_number']
			author = form.data['author']
			dept = form.data['department']
			date = form.data['publication_Date']
			obj = Library(Book_Number=number,
				Book_Name=name,Author=author,Department=dept,
				Publication_Date=date)
			obj.save()
			return HttpResponse("Book Added !")
		else:
			return HttpResponse("Invalid")
	return render(request,'books.html',{'form':form})