from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from .models import Secret
from ..login.models import User
from django.db.models import Count

def secrets(request):
	context = {
		'all_posts': Secret.objects.all(),
		'total_likes': Secret.objects.annotate(total_likes=Count('likes')),
	}
	return render(request, 'secrets/secrets.html', context)

def post(request):
	if request.method == "POST":
		secret_post = request.POST
		person = User.objects.get(id=request.session['id'])
		response = Secret.objects.Valid(secret_post)
	if response['status']:
		Secret.objects.AddWish(secret_post, person)
	return redirect('secrets:secrets')

def deletePost(request, id):
	# Secret.objects.get(id=parameter)
	Secret.objects.get(id=id).delete()
	return redirect('secrets:secrets')

def like(request, id):
	Secret.objects.AddLike(request.session['id'], id)
	return redirect('secrets:secrets')

def popular(request):
	context = {
		'all_posts': Secret.objects.all(),
		'total_likes': Secret.objects.annotate(total_likes=Count('likes')),
	}
	return render(request, 'secrets/popular.html', context)





