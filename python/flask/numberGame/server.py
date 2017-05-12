from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "woo"

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
random.randrange(0, 101) # random number between 0-100


@app.route('/')
def index():
	return render_template("index.html")

app.run(debug=True) # run our server