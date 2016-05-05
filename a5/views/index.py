from flask import render_template
from config import app

@app.route('/a5')
def a5():
    return render_template("a5.html")
