from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def emailCheck():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	else:
		flash("Success!")
	if len(request.form['name']) < 1:
		flash("Name cannot be blank!")
	else:
		flash("Success!")
	if len(request.form['commentArea']) > 120:
		flash("Characters can't exceed 120 characters!")
	session['name'] = request.form['name']
	session['commentArea'] = request.form['commentArea']
	return redirect('/')

   
app.run(debug=True) # run our server