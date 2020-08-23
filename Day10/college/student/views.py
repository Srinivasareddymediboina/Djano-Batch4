from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms import *
from django.contrib import messages

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
		messages.success(request,"Registration Successful")
		return redirect('show')

	return render(request,'register.html')


def signup(req):
	form = StudentForm()
	if req.method=='POST':
		form = StudentForm(req.POST)
		form.save()
		return HttpResponse("Record Saved Successfully")
	return render(req,'signup.html',{'form':form})


def show(request):
	data = Student.objects.all()
	return render(request,'show.html',{'data':data})

def edit(request,id):
	data = Student.objects.get(id=id)
	if request.method=='POST':
		data.Name = request.POST['user']
		data.Age = request.POST['age']
		data.Branch=request.POST['branch']
		data.Mobile = request.POST['phone']
		data.Email = request.POST['mail']
		data.save()
		messages.info(request,"Data Upated")
		return redirect('show')
	return render(request,'edit.html',{'data':data})

def delete(request,id):
	data = Student.objects.get(id=id)
	data.delete()
	messages.warning(request,"User Deleted")
	return redirect("show")
	