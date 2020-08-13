from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import *

# Create your views here.

def register(request):
	if request.method=='POST':
		name = request.POST['user']
		age = request.POST['age']
		branch = request.POST['branch']
		phone = request.POST['phone']
		email = request.POST['mail']

		data = Student(Name=name,Age=age,Branch=branch,Mobile=phone,Email=email)
		data.save()
		return HttpResponse(" Registration Successful")

	return render(request,'register.html')


def signup(req):
	form = StudentForm()
	if req.method=='POST':
		form = StudentForm(req.POST)
		form.save()
		return HttpResponse("Record Saved Successfully")
	return render(req,'signup.html',{'form':form})
