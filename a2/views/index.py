# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template, session, request, redirect
from manager import app
from templates.a2_models import a2_index


@app.route('/orderdetails', methods=['GET'])
def orderdetails():
    ID = request.cookies.get('kitty')
    return render_template("a2/orderdetails.html", userID = 123)


@app.route('/complaint')
def complaint():
    ID = request.cookies.get('kitty')
    return render_template("a2/complaint.html", userID = 123)


@app.route('/orderlist')
def orderlist():
    ID = request.cookies.get('kitty')
    return render_template("a2/orderlist.html", userID = 123)