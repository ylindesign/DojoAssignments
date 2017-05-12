from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form
@app.route('/')
def index():
  # name = request.form['name']
  return render_template("index.html")

# @app.route('/ninjas')
# def ninjas():
#   return render_template("ninjas.html")

# @app.route('/dojos')
# def dojos():
#   return render_template("dojos.html")

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	print name
	return redirect('/')
   
app.run(debug=True) # run our server