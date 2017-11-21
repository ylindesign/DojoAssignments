from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from .models import User


def index(request):
	return render(request, 'login/index.html')

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
		request.session['id'] = response['person'].id
	return redirect('secrets:secrets')

def login(request):
	if request.method == "POST":
		response = User.objects.Login(request.POST)
		if response['status'] == True:
			request.session['user'] = response['user'].first_name
			request.session['id'] = response['user'].id
		return redirect('secrets:secrets')
	else:
		for error in response['errors']:
			messages.error(request, error)
	return redirect('/')

def logout(request):
	request.session.flush()
	return redirect('/')
