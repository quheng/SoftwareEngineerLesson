# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template, session, redirect
from manager import app
from templates.a2_models import a2_index


@app.route('/orderdetails', methods=['GET'])
def orderdetails():
    ID = request.cookies.get('kitty')
    if ID:
        return render_template("a2/orderdetails.html", userID = ID)
    else:
        redirect("http://121.42.175.1/login")

@app.route('/complaint')
def complaint():
    return render_template("a2/complaint.html", userID = 123)

@app.route('/orderlist')
def orderlist():
    return render_template("a2/orderlist.html", userID = 123)
