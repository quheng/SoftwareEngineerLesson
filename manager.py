# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask
import sys
import jinja2
app = Flask(__name__)
app.config.from_object('config')

# database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from models import *
