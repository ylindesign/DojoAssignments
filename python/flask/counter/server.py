from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "woo"



@app.route('/')
def index():
	add()
	return render_template("index.html")

def add():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1
	# return session['counter']


@app.route('/add', methods=['POST'])
def addMore():
	try:
		session['counter'] += 1
	except KeyError:
		session['counter'] = 1
   
	return redirect('/')

@app.route('/remove', methods=['POST'])
def remove():
	session['counter'] = 0
	return redirect('/')

app.run(debug=True) # run our server