import os
from flask import Flask, request, render_template, redirect, url_for, flash, make_response

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login(post=None):
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			flash('Successfully logged in')
			response = make_response(redirect(url_for('welcome', username=request.form.get('username'))))
			response.set_cookie('username', request.form.get('username'))
			return response
		else:
			error = "Username or password incollect"
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	flash('Successfully Logged out.')
	response = make_response(redirect(url_for('login')))
	response.set_cookie('username', '', expires=0)
	return response

def valid_login(username, password):
	return username == password

@app.route('/welcome/<username>')
def welcome(username):
	username = request.cookies.get('username')
	if username:
		return render_template('welcome.html', username=username)
	return redirect(url_for('login'))

if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	app.debug = True
	app.secret_key = 'SuperSecretKey'
	app.run(host=host, port=port)