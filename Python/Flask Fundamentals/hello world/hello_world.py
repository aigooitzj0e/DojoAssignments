from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def success():
	return render_template('index.html', name="Jay")

app.run(debug=True) 