from django.shortcuts import render
from FirstApp.forms import MovieForm
from django.http import HttpResponse
from FirstApp.models import Movies
# Create your views here.

def register(request):
	form=MovieForm(request.POST, request.FILES)
	if form.is_valid():
		form.save()
		return HttpResponse('<h2>Registered Successfully</h2>')

	form=MovieForm()
	return render(request,'register.html',{'form':form})

def login(request):
	if request.method=='POST':
		mname=request.POST['moviename']
		pwd=request.POST['password']
		data=Movies.objects.all().filter(moviename=mname,password=pwd)
		if data:
			return render(request,'homepage.html',)
		else:
			return HttpResponse('Invalid User')
	return render(request,'login.html')