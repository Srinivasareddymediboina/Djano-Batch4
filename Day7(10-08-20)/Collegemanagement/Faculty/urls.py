from django.urls import path
from Faculty import views


urlpatterns=[

	path('index/',views.index,name="index"),
	path('register/',views.register,name="register"),
	

]