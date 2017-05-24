from django.shortcuts import render, redirect
import random, string

def index(request):
	newword = ''.join(random.choice(string.ascii_letters + string.digits) for n in range(15))
	word = {
		'random_word':newword
	}
	return render(request, 'words/html/index.html',word)

def change(request):
	if request.POST:
		if 'counter' in request.session:
			request.session['counter'] += 1
		else:
			request.session['counter'] = 1
	return redirect('/')