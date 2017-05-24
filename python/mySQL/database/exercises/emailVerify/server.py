from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'emails')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    return render_template('index.html', emails=emails)

@app.route('/process', methods=['POST'])
def submit():
    query = "INSERT INTO emails (email) VALUES (:email)"
    data = {
             'email': request.form['email'],
           }
    mysql.query_db(query, data)
    email = request.form['email']

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)