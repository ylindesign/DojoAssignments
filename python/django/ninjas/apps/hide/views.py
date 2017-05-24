from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'hide/index.html')

def ninjas(request):
	return render(request, 'hide/ninjas.html')

def show(request, color):
	context = {
	"color" : color
	}
	# if color == "red":

	return render(request, "hide/show.html", context)