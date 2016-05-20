from manager import db
import json
from sqlalchemy.orm import sessionmaker

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
    def selectOrderByID(ID):
        line = db.session.query(OrderManager).filter(OrderManager.orderID == ID).one()
        temp = {}
        temp['orderAmount'] = line.orderAmount
        temp['buyer'] = line.buyer
        temp['seller'] = line.seller
        temp['orderStatus'] = line.orderStatus
        temp['orderItems'] = line.orderItems
        temp['orderTime'] = line.orderTime.strftime("%Y %m %d %H %M %S")
        return temp

    # @staticmethod
    # def printTable():
    #     table = OrderManager.query.all()
    #     result = []
    #     for line in table:
    #         temp = {}
    #         temp['orderID'] = line.orderID
    #         temp['orderName'] = line.orderName
    #         temp['buyer'] = line.buyer
    #         temp['seller'] = line.seller
    #         temp['orderStatus'] = line.orderStatus
    #         temp['orderItems'] = line.orderItems
    #         temp['orderTime'] = line.orderTime.strftime("%A, %d. %B %Y %I:%M%p")
    #         result.append(temp)
    #     # print result
    #     return result

    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    orderID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    buyer = db.Column(db.Integer)
    seller = db.Column(db.Integer)
    orderAmount = db.Column(db.Float)
    orderItems = db.Column(db.String(200))
    orderStatus = db.Column(db.Integer)
    orderTime = db.Column(db.DateTime)
