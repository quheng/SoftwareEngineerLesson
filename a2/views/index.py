from flask import render_template
from config import app

@app.route('/a2')
def a2():
    return render_template("a2.html")
