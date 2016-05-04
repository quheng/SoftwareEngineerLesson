from a2 import app
from flask import render_template

@app.route("/test")
def test():
    return render_template("index.html")
