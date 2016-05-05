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

# handle error

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
        credentials = credentials
    )
mail_handler.setLevel(logging.ERROR)
app.logger.addHandler(mail_handler)

# log
import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('tmp/paykitty.log', 'a', 1 * 1024 * 1024, 10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info('paykitty error')




