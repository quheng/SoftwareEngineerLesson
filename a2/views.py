from flask import render_template
from a2 import app

@app.route("/")
@app.route('/index')
def index():
    return render_template("index.html")
