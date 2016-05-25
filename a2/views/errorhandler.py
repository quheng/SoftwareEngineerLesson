# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import render_template
from manager import app

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
