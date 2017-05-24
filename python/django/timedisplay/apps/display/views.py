from django.shortcuts import render, HttpResponse
import datetime
  # the index function is called when root is visited
def index(request):
	context = {
	"timenow":datetime.datetime.now()
	}
	return render(request, 'html/index.html', context)