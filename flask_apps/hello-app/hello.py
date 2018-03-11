import os
from flask import Flask, request, render_template, redirect, url_for, flash, make_response, session

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login(post=None):
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			flash('Successfully logged in')
			session['username'] = request.form.get('username')
			return redirect(url_for('welcome'))
		else:
			error = "Username or password incollect"
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	flash('Successfully Logged out.')
	session.pop('username', None)
	return redirect(url_for('login'))

def valid_login(username, password):
	return username == password

@app.route('/')
def welcome():
	if 'username' in session:
		return render_template('welcome.html', username=session['username'])
	return redirect(url_for('login'))

if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	app.debug = True
	app.secret_key = '\x8d\xba\xab\x13\xfb\x15\x98\xe0\x88{\xac\n\xd6>\x02s6\x9b~\xd7\xd3\xcau\xfc'
	app.run(host=host, port=port)