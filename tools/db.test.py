# !/usr/bin/env python
# coding=utf8
# Author: quheng
import sys
sys.path.append("..")

from manager import db
from models import OrderManager
ID = 1
status = 1
line = db.session.query(OrderManager.OrderManager).filter(OrderManager.OrderManager.orderID == ID).update({OrderManager.OrderManager.orderStatus: status})
db.session.commit()
print line
