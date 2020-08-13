from django.urls import path
from student import views

urlpatterns = [
	path('register/',views.register,name='register'),
	path('signup/',views.signup,name='signup'),
]