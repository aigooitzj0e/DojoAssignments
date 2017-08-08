from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def create_user():
	firstname = request.form['first_name']
	lastname = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	confirm = request.form['confirm']

	
	if len(request.form['email']) < 1:
		flash("BOOOOOOIIII.. IF YOU DONT GIVE ME YO EMAIL...")
	if len(request.form['first_name']) < 1:
		flash("BOOOOOOIIII.. IF YOU DONT GIVE ME YO FIRST NAME...")
	if len(request.form['last_name']) < 1:
		flash("BOOOOOOIIII.. IF YOU DONT GIVE ME YO LAST NAME...")
	if len(request.form['password']) < 1:
		flash("BOOOOOOIIII.. IF YOU DONT GIVE ME YO PASSWORD...")
	if len(request.form['confirm']) < 1:
		flash("BOOOOOOIIII.. IF YOU DONT CONFIRM YO PASSWORD...")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address DUMMY!")
	elif len(request.form['password']) < 8:
		flash("BOOOOOOIIII.. 8 CHARACTER MINIMUM PASSWORD...")
	elif password != confirm:
		flash("You're not going to make it far in life, if you can't make matching passwords.")
	else:
		return render_template('results.html', name=firstname+" "+lastname, email=email)
	return redirect('/')
app.run(debug=True) 