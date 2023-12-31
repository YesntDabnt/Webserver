from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def index():
        return "Hejsan"


@app.route("/hello")
def hello_world():
        return "Hello, World"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hej %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return ' %s' % escape(subpath)

@app.route('/add/<int:a>.<int:b>')
def add(a, b):
   return f"svaret blir: {a+b}"
