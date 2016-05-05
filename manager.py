# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask
import sys
import jinja2
app = Flask(__name__)
app.config.from_object('config')


# add template
template_path = []
template_path.append(sys.path[0] + "/a2/templates")
template_path.append(sys.path[0] + "/a5/templates")

template_loader = jinja2.ChoiceLoader([app.jinja_loader, jinja2.FileSystemLoader(template_path), ])
app.jinja_loader = template_loader

# database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from models import *
