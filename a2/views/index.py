# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template, session, redirect
from manager import app
from templates.a2_models import a2_index


@app.route('/orderdetails', methods=['GET'])
def orderdetails():
    return render_template("a2/orderdetails.html", userID = 1)

@app.route('/complaint')
def complaint():
    return render_template("a2/complaint.html", userID = 1)

@app.route('/orderlist')
def orderlist():
    try:
        userID = request.cookies.get("kitty")
        return render_template("a2/orderlist.html", userID = 1)
    except Exception as e:
        return redirect("http://121.42.175.1/login")
