from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

from django.contrib import messages
from .models import Wish
from ..login.models import User

def wish(request):
	context = {
		'user_wishes': Wish.objects.filter(add=User.objects.get(id=request.session['id'])),
		'wished_by': Wish.objects.exclude(add=User.objects.get(id=request.session['id'])),
		# 'wishes': Wish.objects.all(),
		# 'total_likes': Secret.objects.annotate(total_likes=Count('likes')),
	}
	return render(request, 'wish/wish.html', context)

def create(request):
	return render(request, 'wish/create.html')
	# return render(request, 'wish/create.html')

def add(request):
	if request.method == 'POST':
		new_wish = request.POST['wish']
		person = User.objects.get(id=request.session['id'])
		response = Wish.objects.Valid(new_wish)
	if response['status']:
		Wish.objects.AddWish(new_wish, person)
	else:
		for error in response['errors']:
			messages.error(request, error)
		return redirect('wish:create')
	return redirect('wish:wish')

def item(request, id):
	stuff = Wish.objects.get(id=id)
	# stuff.filter
	context = {
		# 'something': id
		'item': stuff
	}
	return render(request, 'wish/item.html', context)

def copy(request, id, item):
	# new_wish = Wish.objects.get(id=id).item
	# print "Wish is: ", new_wish
	person = User.objects.get(id=request.session['id'])
	Wish.objects.CopyWish(id, person)
	return redirect('wish:wish')

def delete(request, id):
	# new_wish = Wish.objects.get(id=id).item
	# print "new wishes name in views: ", new_wish
	# person = User.objects.get(id=request.session['id'])
	Wish.objects.DeleteWish(id)
	return redirect('wish:wish')

def remove(request, id):
	# re_wish = Wish.objects.get(id=id)
	person = User.objects.get(id=request.session['id'])
	Wish.objects.RemoveWish(id, person)
	return redirect('wish:wish')
