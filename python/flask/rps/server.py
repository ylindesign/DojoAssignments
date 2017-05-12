from flask import Flask, render_template, session, flash
app = Flask(__name__)
app.secret_Key = "woo"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/game', methods=['POST'])
def create_user():
   print "Got Post Info"
   session['name'] = request.form['name']
   session['email'] = request.form['email']
   return redirect('/')