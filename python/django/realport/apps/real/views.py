from django.shortcuts import render, HttpResponse
  # the index function is called when root is visited
def index(request):
	# response = "Hello, I am your first request!"
	return render(request, 'real/html/index.html')

def about(request):
	# response = "Hello, I am your first request!"
	return render(request, 'real/html/about.html')

def projects(request):
	# response = "Hello, I am your first request!"
	return render(request, 'real/html/projects.html')

def testimonials(request):
	# response = "Hello, I am your first request!"
	return render(request, 'real/html/testimonials.html')