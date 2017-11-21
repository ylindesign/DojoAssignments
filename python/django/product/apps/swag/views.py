from django.shortcuts import render, redirect
from .models import Stuff


def index(request):
	context = {
	"stuff" : Stuff.objects.all()
	}
	return render(request, "swag/index.html", context)

def show(request):
	Stuff.objects.create(name=request.POST['name'], description=request.POST['description'], weight=request.POST['weight'], price=request.POST['price'], cost=request.POST['cost'], category=request.POST['category'])
	stuff = Stuff.objects.all()
	print stuff
	return redirect("/")

