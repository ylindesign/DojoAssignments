from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

# from .models import MODELCLASS
from django.contrib import messages
from ..users.models import User
from .models import Create

def createpost(request):
	# if request.method == "POST":
	# 	response_from_models = Post.objects.Save(request.POST)

	secret = {
		'user_secret': request.POST['content'],
	}

	print "*"*20
	print "content: ", secret['user_secret']
	# this_user = Create.objects.get(user = request.session['email'])
	# print "this user: ", this_user.first_name
	Create.objects.create(content=request.POST['content'])
	return redirect("users:secrets")

def index(request):
	context = {
		'all_posts': Create.objects.all(),
	}
	return render(request, 'users/secrets.html', context)


