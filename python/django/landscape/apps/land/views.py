from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'land/index.html')

def snow(request):
	return render(request, 'land/snow.html')

def desert(request):
	return render(request, 'land/desert.html')

def forest(request):
	return render(request, 'land/forest.html')

def vine(request):
	return render(request, 'land/vine.html')

def trop(request):
	return render(request, 'land/trop.html')

# I know what I did wrong, but I want to move on!