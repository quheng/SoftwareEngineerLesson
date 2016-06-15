# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template, session, request, redirect
from manager import app
from templates.a2_models import a2_index


@app.route('/orderdetails', methods=['GET'])
def orderdetails():
    ID = request.cookies.get('kitty')
    if ID:
        return render_template("a2/orderdetails.html", userID = ID)
    else:
        return redirect("http://121.42.175.1/login")


@app.route('/complaint')
def complaint():
    ID = request.cookies.get('kitty')
    if ID:
        return render_template("a2/complaint.html", userID = ID)
    else:
        return redirect("http://121.42.175.1/login")


@app.route('/orderlist')
def orderlist():
    ID = request.cookies.get('kitty')
    if ID:
        return render_template("a2/orderlist.html", userID = ID)
    else:
        return redirect("http://121.42.175.1/login")