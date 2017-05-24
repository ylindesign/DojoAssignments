from django.shortcuts import render, HttpResponse
  # the index function is called when root is visited
def index(request):
	# response = "Hello, I am your first request!"
	return render(request, 'face/index.html')

def testimonials(request):
	# response = "Hello, I am your first request!"
	return render(request, 'face/testimonials.html')