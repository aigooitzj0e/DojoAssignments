from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

winning_num = random.randrange(0, 101)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	guess = request.form['guess_area']
	message = ""

	print guess, winning_num
	if int(guess) == winning_num:
		message = "You win!"

	elif int(guess) > winning_num:
		message = "Lower!"

	elif int(guess) < winning_num:
		message = "Higher!"
	return render_template('index.html', message=message)


app.run(debug=True) 
