from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  # name = request.form['name']
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def results():
	name = request.form['name']
	return render_template("results.html", name=name)

   
app.run(debug=True) # run our server