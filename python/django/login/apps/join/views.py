from django.shortcuts import render, HttpResponse, redirect

from .models import MODELCLASS

def index(request):
	return render(request, 'appname/index.html')

def process(request):
	return render(request, 'appname/index.html')
