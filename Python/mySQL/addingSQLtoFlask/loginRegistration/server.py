from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'
mysql = MySQLConnector(app, "registerLogin")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT password, id FROM users WHERE email = :email"
    email_results = mysql.query_db(query, {'email': request.form['email']})

    user_dict = email_results[0]
    encrypted_password = md5.new(request.form['password']).hexdigest()

    if encrypted_password == user_dict['password']:
        return redirect('/results')

    flash("Wrong Password!")
    return redirect('/')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/register_page', methods=['GET'])
def register_page():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }

    if len(request.form['email']) < 1:
        flash("Enter an Email")
    if len(request.form['first_name']) < 1:
        flash("Enter First Name")
    if len(request.form['last_name']) < 1:
        flash("Last Name")
    if len(request.form['password']) < 1:
        flash("Enter Password")
    if len(request.form['confirm']) < 1:
        flash("Confirm Pasword")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    elif len(request.form['password']) < 8:
        flash("Password must be 8 characters minimum")
    elif request.form['password'] != request.form['confirm']:
        flash("Passwords do not match!")
    else:
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password,
        }

        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
        mysql.query_db(query, data)
        return render_template('results.html', name=request.form['first_name']+" "+request.form['last_name'], email=request.form['email'])


    mysql.query_db(query, data)
    return redirect('/register_page')



app.run(debug=True)
