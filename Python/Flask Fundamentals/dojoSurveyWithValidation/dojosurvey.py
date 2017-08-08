from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
	name = request.form['name']
	location = request.form['location']
	lang = request.form['lang']
	comment = request.form['comment']

	if len(request.form['name']) < 1:
		flash("Did you forget your name? ")
	elif len(request.form['comment']) < 1:
		flash("You forgot your comment!")
	elif len(request.form['comment']) > 120:
		flash("I didn't ask for your life story!")
	else:
		return render_template('results.html', name=name, location=location, lang=lang, comment=comment)
	return redirect('/')
app.run(debug=True) 