# !/usr/bin/env python
# coding=utf8
# Author: quheng

from flask import Flask, redirect
import sys
import jinja2
app = Flask(__name__, static_path = '/a2static')
app.config.from_object('config')

# database
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
from models import *

# api
import api
@app.route('/docs')
def docs():
    return redirect('/static/docs.html')

# handle error
import os
basedir = os.path.abspath(os.path.dirname(__file__))



@app.route('/insert')
def insert():
    api.order.insertOrder.insert("ID4",  "Name",  "buyer2",  "seller2",  "Items")
    return 'Hello World'

@app.route('/select')
def select():
    result = api.order.selectOrder.select("ID");
    html = ""
    for x in result:
        temp = x.orderID
        html += str(temp) + '\n'
    return html

# admin
from admin import admin_manager

# send email
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
import logging
from logging.handlers import SMTPHandler
credentials = None
if MAIL_USERNAME or MAIL_PASSWORD:
    credentials = (MAIL_USERNAME, MAIL_PASSWORD)
mail_handler = SMTPHandler(
        mailhost = MAIL_SERVER,
        fromaddr = MAIL_USERNAME,
        toaddrs = ADMINS,
        subject = 'Paykitty Bug Reporter',
        credentials = credentials)
mail_handler.setLevel(logging.ERROR)
app.logger.addHandler(mail_handler)

# log
import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler(basedir + '/tmp/paykitty.log', 'a', 1 * 1024 * 1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info('paykitty error')
