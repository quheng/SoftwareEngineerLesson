# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template
from manager import app
from templates.a2_models import a2_index
from models import user

@app.route('/')
@app.route('/index')
def index():
    return render_template("index/index.html")

@app.route('/orderdetails')
def orderdetails():
    return render_template("a2/orderdetails.html")

@app.route('/complaint')
def complaint():
    return render_template("a2/complaint.html")

@app.route('/orderlist')
def orderlist():
    return render_template("a2/orderlist.html")

@app.route('/a2')
def a2():
    return render_template("a2/a2.html")


@app.route('/bug')
def bug():
    temp_ata = a2_index.data()
    temp_data.userlist = user.User.get_users()
    return render_template("a2/bug.html", data = temp_data)
