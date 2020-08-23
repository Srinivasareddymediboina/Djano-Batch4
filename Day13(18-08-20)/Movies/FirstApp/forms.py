from FirstApp.models import Movies
from django.forms import ModelForm
from django import forms
class MovieForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=Movies
		fields="__all__"