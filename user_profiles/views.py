from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import LoginForm, RegistrationForm

# Create your views here.

def handler404(request):
	return render(request, '404.html')

def handler403(request):
	return render(request, '403.html')

def handler500(request):
	return render(request, '500.html')

@login_required(login_url='/app/login/')
def dashboard(request):
	"""
	Dashboard View
	"""
	if request.user.is_authenticated():
		title = "Welcome %s !" %(request.user)
		context = {
			"template_title": title
		}
		return render(request, "dashboard.html", context)
	else:
		return redirect('/app/login')


def login(request):
	"""
	Login View
	"""

	if(request.method == 'POST'):
		form =  LoginForm(data=request.POST)
		if form.is_valid():
			user = authenticate(email=request.POST['email'], password=request.POST['password'])
			if user is not None:
				if user.is_active:
					django_login(request, user)
					return redirect('/app/dashboard', request)
			else:
				form = LoginForm()
				return render_to_response('login.html', {
					'form' : form,
					'login_error_message' : 'Invalid Login Credentials',
				}, context_instance=RequestContext(request))
	else:
		form = LoginForm()

	return render_to_response('login.html', {
		'form' : form,
	}, context_instance=RequestContext(request))


def register(request):
	"""
	User Registration Form
	"""
	if(request.method == 'POST'):
		form = RegistrationForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('/app/dashboard')
	else:
		form = RegistrationForm()

	return render_to_response('register.html', {
		'form' : form
	}, context_instance=RequestContext(request))

def logout(request):
	"""
	Logout view
	"""
	django_logout(request)
	return redirect('/app/login')
