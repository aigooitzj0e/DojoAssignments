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
    return redirect('/success')

@app.route('/success')
def results():
    if 'id' not in session:
        return redirect('/')
    return render_template('results.html')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT password, salt, id FROM users WHERE email = :email"
    email_results = mysql.query_db(query, {'email': request.form['email']})

    if len(email_results) == 0:
        flash("You are not registered.")
        return redirect('/')

    user_dict = email_results[0]
    encrypted_password = md5.new(request.form['password'] + user_dict['salt']).hexdigest()

    if encrypted_password == user_dict['password']:
        session['id'] = user_dict['id']
        return redirect('/success')

    flash("Wrong password!")
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def wall():
    print(session['users'])
    if 'users' in session:
        query = "SELECT first_name, last_name, message_text, DATE_FORMAT(messages.created_at, '%M %D %Y %H:%i') AS created_at, messages.id, user_id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
        message_list = mysql.query_db(query)
        #print(message_list)
        query = "SELECT first_name, last_name, comment_text, DATE_FORMAT(comments.created_at, '%M %D %Y %H:%i') AS created_at, message_id FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.created_at"
        comment_list = mysql.query_db(query)
        #print(comment_list)
        return render_template('/wall.html', message_list = message_list, comment_list = comment_list)
    else:
        flash("You are not logged in")
        return redirect('/')

@app.route('/wall/message', methods=['POST'])
def add_message():
    message_text = request.form['message']
    query = "INSERT INTO messages (message_text, created_at, updated_at, user_id) VALUES (:message_text, Now(), Now(), :user_id)"
    data = {
        'message_text': message_text,
        'user_id': session['users']['id']
    }
    mysql.query_db(query, data)
    return redirect('/wall')
@app.route('/wall/comment/<message_id>', methods=['POST'])
def add_comment(message_id):
    query = "INSERT INTO comments (comment_text, created_at, updated_at, user_id, message_id) VALUES (:comment_text, Now(), Now(), :user_id, :message_id)"
    data = {
        'comment_text': request.form['comment'],
        'user_id': session['users']['id'],
        'message_id': message_id
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall/message/delete/<id>')
def delete_comment(id):
    del_comments_query = "DELETE FROM comments WHERE message_id = :id"
    data = {
        'id': id
    }
    mysql.query_db(del_comments_query, data)
    del_message_query = "DELETE FROM messages WHERE id = :id"
    mysql.query_db(del_message_query, data)
    return redirect('/wall')
















app.run(debug=True)
