from django.urls import path
from student import views

urlpatterns = [
	path('register/',views.register,name='register'),
	path('signup/',views.signup,name='signup'),
	path('show/',views.show,name='show'),
	path('edit/<int:id>',views.edit,name='edit'),
	path('delete/<int:id>',views.delete,name='delete'),
]