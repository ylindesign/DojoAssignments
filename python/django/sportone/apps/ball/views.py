from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from .models import MODELCLASS

def index(request):
	return render(request, 'ball/index.html')
