from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .scrape import search
# Create your views here.

def home(request):
	return render(request,"home.html",{})

def init_login(request):
	template_path='app1/signin.html'
	context={}
	return render(request,template_path,context)

def login_view(request):

	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username= username ,password=password)
	if user is not None and user.is_active:
		auth.login(request,user)
		search()
		return HttpResponse("Successfully Logged In")
	else:
		return HttpResponse("INVALID")
def logout_view(request):
	auth.logout(request)
	return HttpResponse("Logout successful")

def register(request):
	template_path='app1/register.html'
	context = {}
	return render(request,template_path,context)

def register_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email= request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create_user(username,email,password)
		user.save()
		return HttpResponseRedirect(reverse('init_login',args=[]))
	template_path='app1/register.html'
	context = {}
	return render(request,template_path,context)

