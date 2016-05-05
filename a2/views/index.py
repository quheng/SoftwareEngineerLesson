# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template
from manager import app

@app.route('/a2')
def a2():
    return render_template("a2.html")
