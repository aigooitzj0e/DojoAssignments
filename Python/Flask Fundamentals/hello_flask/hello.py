from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    
                         
@app.route('/')          
  return 'Hello World!'  
  
@app.route('/success')
def success():
	return render_template('success.html')

app.run(debug=True) 