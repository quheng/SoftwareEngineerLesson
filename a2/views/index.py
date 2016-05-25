# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template
from manager import app
from templates.a2_models import a2_index


@app.route('/orderdetails', methods=['GET'])
def orderdetails():
    return render_template("a2/orderdetails.html", userID)

@app.route('/complaint')
def complaint():
    return render_template("a2/complaint.html", userID)

@app.route('/orderlist')
def orderlist():
    return render_template("a2/orderlist.html", userID)
