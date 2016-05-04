from a2 import app
from flask import render_template
from templates.model import user

@app.route("/")
@app.route('/index')
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    user = user.user()
    user.name = "tom"
    user.password = "123456"
    return render_template("login.html", user = user)
