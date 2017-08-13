from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re, os, binascii, md5

app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'
mysql = MySQLConnector(app, "registerLogin")
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register_page')
def regpage():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    ourData = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm': request.form['confirm']
    }

    error = False
    for value in ourData.itervalues():
        if value == '':
            error = True
            break
    if error == True:
        flash("All fields must be completed")

    if not ourData['first_name'].isalpha() or not ourData['last_name'].isalpha():
        flash("First and Last Name must be letters only")
        error = True

    if len(ourData['first_name']) < 2 or len(ourData['last_name']) < 2:
        flash("Your name needs to be longer than 1 letter")
        error = True

    if not EMAIL_REGEX.match(ourData['email']):
        flash("Invalid email address")
        error = True

    if len(ourData['password'])	< 8:
        flash("Password too short. Min 8 characters")
        error = True

    if ourData['password'] != ourData['confirm']:
        flash("Passwords don't match")
        error = True

    query = "SELECT email FROM users WHERE email = :email"
    email_results = mysql.query_db(query, {'email': ourData['email']})
    if len(email_results) != 0:
        error = True
        flash("You've already registered. Login.")

    if error == True:
        return redirect('/')

    salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(ourData['password'] + salt).hexdigest()
    ourData['salt'] = salt
    ourData['password'] = hashed_pw
    ourData.pop('confirm')


    query = "INSERT INTO users (first_name, last_name, email, password, salt) VALUES(:first_name, :last_name, :email, :password, :salt)"
    user_id = mysql.query_db(query,ourData)

    session['id'] = user_id
    return redirect('/')

@app.route('/success')
def results():
    if 'id' not in session:
        return redirect('/')
    return render_template('results.html')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT password, salt, id, first_name FROM users WHERE email = :email"
    email_results = mysql.query_db(query, {'email': request.form['email']})

    if len(email_results) == 0:
        flash("You are not registered.")
        return redirect('/')

    user_dict = email_results[0]
    encrypted_password = md5.new(request.form['password'] + user_dict['salt']).hexdigest()
    name = user_dict['first_name']
    print name

    if encrypted_password == user_dict['password']:
        session['id'] = user_dict['id']
        # return redirect('/success')
        return render_template('results.html', name=name)

    flash("Wrong password!")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
