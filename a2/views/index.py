# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template
from manager import app
from templates.a2_models import a2_index
from models import user

@app.route('/a2')
def a2():
    temp_ata = a2_index.data()
    temp_data.userlist = user.User.get_users()
    return render_template("a2/a2.html", data = temp_data)
