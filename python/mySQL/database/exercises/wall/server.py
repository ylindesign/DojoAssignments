from flask import Flask, redirect, request, session, render_template, flash
app = Flask(__name__)
from mysqlconnection import MySQLConnector
mysql = MySQLConnector(app, 'wall_db')
app.secret_key = 'this is top secret'
import md5 # imports the md5 module to generate a hash


import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/wall')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # validate the form input
    # store errors in list
    errors = []

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    # complete the validations

    if not  first_name.isalpha():
        errors.append('First name field must be characters only!')
    if len(first_name) < 2:
        errors.append('First name field must be at least 2 characters long!')

    if not  last_name.isalpha():
        errors.append('Last name field must be characters only!')
    if len(last_name) < 2:
        errors.append('Last name field must be at least 2 characters long!')

    if not len(email):
        errors.append("Email can't be blank")
    if not EMAIL_REGEX.match(email):
        errors.append('Email must be valid')

    if len(password) < 8:
        errors.append('Password must be at least 8 characters long!')
    if not password == password_confirmation:
        errors.append('Passwords must match!')

    query = 'SELECT * FROM users WHERE email = :email'
    data = {
        'email':email
    }
    user = mysql.query_db(query, data)

    if user:
        errors.append('Email is already taken!')

    # check errors list
    if errors:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        # save the user in db
        hashed_password = md5.new(password).hexdigest()

        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        data = {
            'first_name':first_name,
            'last_name':last_name,
            'email': email,
            'password': hashed_password
        }

        session['user_id'] = user
        return redirect('/wall')

@app.route('/wall')
def success():
    if not 'user_id' in session:
        return redirect('/')

    # query = "SELECT message FROM messages WHERE message = :message LIMIT 1"
    # data = {
    #     'message':session['message']
    # }
    # session['messages'] = mysql.querydb(query, data)
    query = 'SELECT * FROM messages.content, DATE_FORMAT(messages.created_at, "%M%D, %Y") AS date, CONCAT(users.first_name, " ", users.last_name) AS full_name FROM messages JOIN users on sers.id = messages.user_id'
    messages = mysql.query_db(query)
    return render_template('wall.html', messages = messages)

@app.route('/postm', methods=['POST'])
def postMessage():
    query = "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())"
    data = {
            'message':request.form['message'],
            'user_id':session['user_id']
        }
    # messages = 
    mysql.query_db(query, data)
    # session['messages'] = user
    return redirect('/wall')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    # get a user from the DB
    query = 'SELECT * FROM users WHERE email = :email'
    data = {
        'email':request.form['email']
    }
    user = mysql.query_db(query, data)
    if user:
        # continue with the login
        hashed_password = md5.new(request.form['password']).hexdigest()
        if user[0]['password'] == hashed_password:
            session['user_id'] = user[0]['id']
            return redirect('/wall')
        else:
            flash('Invalid email/password combination!')
            return redirect('/')

    else:
        flash("Email doesn't exist")
        return redirect('/')

app.run(debug = True)