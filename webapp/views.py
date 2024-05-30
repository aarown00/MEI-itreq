from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from. models import IT_Request

def home(request):
	it_requests = IT_Request.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Successfully Logged In!")
			return redirect('home')
		else:
			messages.error(request, "Account credentials is invalid. Please try again or register.")
			return redirect('home')
	else:
		return render(request, 'home.html', {'it_requests': it_requests})






def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Successfully Logged Out!")
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
		
		
	else:
		form = RegisterForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def addrequest_user(request):
    it_requests = IT_Request.objects.all()
    messages.success(request, "Request Added!")
    return render(request, 'home.html', {'it_requests': it_requests})


