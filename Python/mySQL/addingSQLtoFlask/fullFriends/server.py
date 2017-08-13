from flask import Flask, request, redirect, render_template
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'fullFriends')
# an example of running a query

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users=users)


@app.route('/users', methods=['POST'])
def create():
    query = 'INSERT INTO users (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())'
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)


#=========================================================
#Displays in terminal all the friends in DB

# @app.route('/')
# def index():
#     users = mysql.query_db("SELECT * FROM users")
#     print users
#     return render_template('index.html')
#=========================================================
#Check to see if name and age fields prints to terminal
#if it prints its sending info to db

# @app.route('/users', methods=['POST'])
# def create():
#     print request.form['name']
#     print request.form['age']
#     return redirect('/')
#=========================================================
