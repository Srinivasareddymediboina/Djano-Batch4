from django.forms import ModelForm
from FirstApp.models import Email

class EmailForm(ModelForm):
	class Meta:
		model=Email
		fields=['firstname','lastname','Email','username','img']
