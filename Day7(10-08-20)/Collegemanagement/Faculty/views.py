from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req,"Faculty/index.html")

def register(req):
	if req.method=="POST":
		print("one")
		a=req.POST['username1']
		b=req.POST['age']
		c=req.POST['email']
		return render(req,'Faculty/showdata.html',{'a':a,'b':b,'c':c})

	return render(req,"Faculty/register.html")