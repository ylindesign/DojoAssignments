from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "woo"

import random 
random.randrange(0, 101) # random number between 0-100


@app.route('/')
def index():
	if not "gold" in session:
		session['gold'] = 0
		# session['results'] = ''
	if not "list" in session:
		session['list'] = []
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process():
	
	if request.form['building'] == "farm":
		add = random.randrange(10, 21)
		session['gold'] += add
		earn = "Earned "
		earn += str(add)
		earn += " gold from the farm."
		session['list'].append(earn)
	elif request.form['building'] == "cave":
		add = random.randrange(5, 11)
		session['gold'] += add
		earn = "Earned "
		earn += str(add)
		earn += " gold from the cave."
		session['list'].append(earn)
	elif request.form['building'] == "house":
		add = random.randrange(2, 6)
		session['gold'] += add
		earn = "Earned "
		earn += str(add)
		earn += " gold from the house."
		session['list'].append(earn)
	elif request.form['building'] == "casino":
		chance = random.randrange(0,2)
		if chance == 0:
			session['gold'] += 50
			earn = "Earned 50 gold from the casino."
		elif chance == 1:
			session['gold'] -= 50
			earn = "Lost 50 gold from the casino."
		
		session['list'].append(earn)
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')


app.run(debug=True) # run our server