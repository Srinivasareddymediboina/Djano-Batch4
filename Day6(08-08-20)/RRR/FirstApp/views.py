from django.shortcuts import render

# Create your views here.

def home(request):

	return render(request,'home.html')

def index(request):

	return render(request, 'index.html')

def forms(request):

	return render(request, 'forms.html')