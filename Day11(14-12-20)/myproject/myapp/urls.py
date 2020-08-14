from django.urls import path
from myapp import views # from . import views

urlpatterns = [
	path('addbook/',views.addBook,name='books'),
]