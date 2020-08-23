from django.shortcuts import render
from EamilSend import settings
from django.core.mail import send_mail
from django.http import HttpResponse
import random
from FirstApp.forms import EmailForm
from FirstApp.models import Email
from django.core.mail import EmailMessage

# Create your views here.
def message(request):
	if request.method=='POST':
		tomail=request.POST['email']
		sub=request.POST['subject']
		msg=request.POST['message']
		sender=settings.EMAIL_HOST_USER
		receiver=tomail
		send_mail(sub,msg,sender,[receiver])
		return HttpResponse('<h1>Email Send Successfully</h1>')
	return render(request,'message.html')


'''def register(request):
	if request.method=='POST':
		fname=request.POST['firstname']
		lname=request.POST['lastname']
		email=request.POST['email']
		uname=request.POST['username']
		password=fname[:2]+str(random.randint(100000,999999))+lname[:2]
		Email.objects.create(firstname=fname,lastname=lname,Email=email,
			username=uname,password=password)
		sub="Reg to your Login details..."
		body="""Hello {} \n\n This is Your Username: {}\n\n Your Password: {}\n\n """.format(uname,uname,password)
		sender=settings.EMAIL_HOST_USER
		receiver=email
		send_mail(sub,body,sender,[receiver])
		return HttpResponse('<h1>Please Check your Eamil id for login details</h1>')

	return render(request,'sendmail.html')'''
def register(request):
	if request.method=='POST':
		form=EmailForm(request.POST,request.FILES)
		if form.is_valid():
			username=request.POST['username']
			password=str(random.randint(100000,999999))
			receiver=request.POST['Email']
			sender=settings.EMAIL_HOST_USER
			sub="Reg to your Login details..."
			body="""Hello {} \n\n This is Your Username: {}\n\n 
			Your Password: {}\n\n """.format(username,username,password)
			email=EmailMessage(sub,body,sender,[receiver])
			email.content_subtype='html'
			file=request.FILES['img']
			email.attach(file.name,file.read(),file.content_type)
			email.send()
			form.save()
			return HttpResponse('Done')
	form=EmailForm()
	return render(request,'sendmail.html',{'form':form})
































'''def attachment(req):
	if req.method=="POST":
		sub=req.POST['subject']
		msg=req.POST['body']
		mailid=req.POST['email']
		frommail=EMAIL_HOST_USER
		email=EmailMessage(sub,msg,EMAIL_HOST_USER,[mailid])
		email.content_subtype='html'
		file=req.FILES['files']
		email.attach(file.name,file.read(),file.content_type)
		email.send()
		return render(req,'mailsendwelcomepage.html',{'mailid':mailid})
	return render(req,'documentupload.html')'''