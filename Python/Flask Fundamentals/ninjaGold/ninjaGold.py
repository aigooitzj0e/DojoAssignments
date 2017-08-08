from flask import Flask, render_template, redirect, request, session
import random
import time

app = Flask(__name__)

app.secret_key = 'ThisIsASecret'

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    if "activities" not in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    localtime = time.asctime( time.localtime(time.time()))
    print localtime
    print (building)

    if building == "farm":
        newgold = random.randint(10,20)
    elif building == "cave":
        newgold = random.randint(5,10)
    elif building == "house":
        newgold = random.randint(2,5)
    elif building == "casino":
        newgold = random.randint(-50, 50)

    session['gold'] += newgold

    if newgold < 0:
        session['activities'].insert(0, {"color":"Entered a Casino and lost {} gold... Sucks to suck... {}".format(newgold, localtime), "class":"red"})

    else:
        session['activities'].insert(0, {"color":"Earned {} gold from the {}! {}".format(newgold, building, localtime), "class":"green"})

    print newgold

    return redirect('/')


app.run(debug=True)
