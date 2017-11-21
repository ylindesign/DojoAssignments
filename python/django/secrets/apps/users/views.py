from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from .models import User
from ..post.models import Create

def index(request):
	if "first_name" in request.session:
		return redirect('/secrets')
	return render(request, 'users/index.html')

def register(request):
	person = {
		'first_name': request.POST['first_name'],
		'last_name': request.POST['last_name'],
		'email': request.POST['email'],
		'password': request.POST['password'],
		'conf_pw': request.POST['conf_pw'],
	}

	if request.method != "POST":
		messages.add_message(request, messages.ERROR, "Cant have an empty form")
		return redirect("/")

	response = User.objects.Regis(person)

	if response['status'] == False:
		for error in response['errors']:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/")
	else:
		messages.add_message(request, messages.SUCCESS, "You have registered!" )
		request.session["first_name"] = person["first_name"]
		return redirect("/secrets")

def login(request):
	if request.method != "POST":
		messages.add_message(request, messages.ERROR, "Cant leave fields blank")
		return redirect("/")

	person = {
		"email" : request.POST["email_login"],
		"password" : request.POST["pw_login"],
	}

	response = User.objects.Valid(person)

	if response["status"] == True:
		request.session["first_name"] = response["user"].first_name
		request.session["email"] = response["user"].email
		messages.add_message(request, messages.SUCCESS, "You have logged in!" )
		return render(request, 'users/secrets.html', person)
	else:
		messages.add_message(request, messages.ERROR, "Invalid Login")
		return redirect("/")

def logout(request):
	request.session.flush()
	return redirect("/")

def secrets(request):
	context = {
		'all_posts': Create.objects.all(),
		# 'user_info': User.objects.get(email=request.session["email"]),
	}
	return render(request, 'users/secrets.html', context)
	# return render(request, 'users/secrets.html')