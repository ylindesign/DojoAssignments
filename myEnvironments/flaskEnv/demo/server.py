from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
# def index():
# 	print "in index method"
	# return "message from server"


def hello_world():
	return render_template('index.html')

app.run(debug=True)