from django.shortcuts import render, HttpResponse, redirect

values = ['hey', 'test', 'whoa']

def index(request):
	if 'user' in request.session:
		request.session.flush()
	return render(request, 'pick/index.html')

def results(request):
	if request.method == "POST":
		request.session['user'] = request.POST['user']
	return redirect('/show')

def show(request):
	request.session['new'] = []
	numnum = int(request.session['user'])
	for x in xrange(0, numnum):
		request.session['new'].append(values[x])
	return render(request, 'pick/show.html')
