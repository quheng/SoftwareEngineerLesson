# !/usr/bin/env python
# coding=utf8
# Author: quheng

from manager import db
from models import *
u = user.User(nickname='Tom', email='tom@email.com')
db.session.add(u)
db.session.commit()
users = user.User.query.all()
print users
