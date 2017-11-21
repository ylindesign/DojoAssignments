from django.shortcuts import render, HttpResponse, redirect
from .models import Book


def index(request):
	context = {
	"bookie" : Book.objects.all()
	}
	return render(request, 'book/index.html', context)


def show(request):
	Book.objects.create(title=request.POST['title'], author=request.POST['author'], dates=request.POST['dates'], category=request.POST['category'])
	bookie = Book.objects.all()
	return redirect("/")
