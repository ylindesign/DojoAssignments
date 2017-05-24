from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "woo"

import random 
random.randrange(0, 101) # random number between 0-100


@app.route('/')
def index():
	if not "random" in session:
		session['random'] = random.randrange(0, 101)
	return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
	session['guess'] = int(request.form['guess'])
	print session['guess']
	# if session['guess'] > session['random']:
	# 	session['rank'] = "High"
	# 	return redirect('/')
	# elif session['guess'] < session['random']:
	# 	session['rank'] = "Low"
	# 	return redirect('/')
	# else:
	# 	return redirect('/')
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	# session['random'] = random.randrange(0, 101)
	return redirect('/')


app.run(debug=True) # run our server