from django.shortcuts import render, HttpResponse, redirect

from .models import Lecture

def index(request):
	context = {
	"course" : Lecture.objects.all()
	}
	return render(request, 'class/index.html', context)

def destroy(request, id):
	context = {
	"class" : Lecture.objects.get(id=id)
	}
	return render(request, "class/destroy.html", context)

def process(request):
	Lecture.objects.create(name=request.POST['name'], description=request.POST['description'])
	course = Lecture.objects.all()
	return redirect("/")

def remove(request, id):
	if request.method == "POST": 
		if request.POST['yes']:
			Lecture.objects.filter(id=id).delete()
	return redirect("/")

