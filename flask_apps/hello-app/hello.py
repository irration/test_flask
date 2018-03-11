import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Index Page"

@app.route('/hello')
def hello_world():
	i = 3
	return "You've visited " + str(i) + " times"

@app.route('/user/<username>')
def show_user_profile(username):
	# show the user profile for that user
	return "User %s" % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return "Post %d" % post_id

if __name__ == '__main__':
	host = os.getenv('IP', '0.0.0.0')
	port = int(os.getenv('PORT', 5000))
	app.debug = True
	app.run(host=host, port=port)