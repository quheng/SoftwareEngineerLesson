# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template
from models import user
from manager import app
from a2_models import a2_index

@app.route('/a2')
def a2():
    temp_data = a2_index.data()
    temp_data.userlist = user.User.get_users()
    return render_template("a2.html", data = temp_data)
