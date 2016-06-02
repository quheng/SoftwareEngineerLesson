from manager import db
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
import requests

class OrderManager(db.Model):
    """docstring for OrderManager"""
    def __init__(self):
        super(OrderManager, self).__init__()

    # @staticmethod
    # def delete(ID):
    #     temp = OrderManager.query.filter(OrderManager.orderID == ID).first()
    #     db.session.delete(temp)
    #     db.session.commit()
    #

    @staticmethod
    def insertOrder(newOrder):
        db.session.add(newOrder)
        db.session.commit()

    @staticmethod
    def UpdateOrderState(ID, status):
        db.session.query(OrderManager).filter(OrderManager.orderID == ID).update({OrderManager.orderStatus: status})
        db.session.commit()

    @staticmethod
    def selectOrderByUser(ID):
        line = db.session.query(OrderManager).filter(or_(OrderManager.buyer == ID, OrderManager.seller == ID)).all()
        res = []
        for item in line:
            tem = {}
            tem['orderID'] = item.orderID
            res.append(tem)
        return res

    @staticmethod
    def selectAllOrder(ID):
        line = db.session.query(OrderManager).filter(or_(OrderManager.buyer == ID, OrderManager.seller == ID)).all()
        res = []
        for item in line:
            tem = {}
            tem['orderID'] = item.orderID
            tem['orderAmount'] = item.orderAmount
            tem['buyer'] = item.buyer
            tem['seller'] = item.seller
            tem['orderStatus'] = item.orderStatus
            tem['orderItems'] = item.orderItems
            tem['orderTime'] = item.orderTime.strftime("%Y-%m-%d %H:%M:%S")
            res.append(tem)
        return res

    @staticmethod
    def getOrderListByDate(start, end):
        line = db.session.query(OrderManager).filter(and_(OrderManager.orderTime < end, OrderManager.orderTime > start)).all()
        res = []
        for item in line:
            tem = {}
            tem['orderID'] = item.orderID
            tem['orderAmount'] = item.orderAmount
            tem['buyer'] = item.buyer
            tem['seller'] = item.seller
            tem['orderStatus'] = item.orderStatus
            tem['orderItems'] = item.orderItems
            tem['orderTime'] = item.orderTime.strftime("%Y-%m-%d %H:%M:%S")
            res.append(tem)
        return res

    @staticmethod
    def selectOrderByCondition(c):
        query = db.session.query(OrderManager).filter(or_(OrderManager.buyer == c.userID, OrderManager.seller == c.userID))
        if (int(c.status) != -1):
            query = query.filter(OrderManager.orderStatus == c.status)
        else:
            query = query.filter(OrderManager.orderStatus > -1)

        date = datetime.utcnow()
        if (int(c.date) == -1):
            date = date - relativedelta.relativedelta(years=1000)
        elif(int(c.date) == 0):
            date -= relativedelta.relativedelta(days=1)
        elif(int(c.date) == 1):
            date -= relativedelta.relativedelta(weeks=1)
        elif(int(c.date) == 2):
            date -= relativedelta.relativedelta(months=1)
        elif(int(c.date) == 3):
            date -= relativedelta.relativedelta(years=1)
        query = query.filter(OrderManager.orderTime > date)

        if (int(c.sort) == 0):
            line = query.order_by(OrderManager.orderTime.desc()).all()
        else:
            line = query.order_by(OrderManager.orderStatus).all()

        res = []
        for item in line:
            tem = {}
            tem['orderID'] = item.orderID
            res.append(tem)
        return res

    @staticmethod
    def selectOrderByID(ID):
        line = db.session.query(OrderManager).filter(OrderManager.orderID == ID).one()
        temp = {}
        temp['orderAmount'] = line.orderAmount
        temp['buyer'] = line.buyer
        temp['seller'] = line.seller
        temp['orderStatus'] = line.orderStatus
        temp['orderItems'] = line.orderItems
        temp['orderTime'] = line.orderTime.strftime("%Y-%m-%d %H:%M:%S")
        return temp

    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    orderID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    buyer = db.Column(db.Integer)
    seller = db.Column(db.Integer)
    orderAmount = db.Column(db.Float)
    orderItems = db.Column(db.String(200))
    orderStatus = db.Column(db.Integer)
    orderTime = db.Column(db.DateTime)

class OrderCondition(object):
    def __init__(self):
        userID = -1
        date = 0
        status = -1
        sort = 0
