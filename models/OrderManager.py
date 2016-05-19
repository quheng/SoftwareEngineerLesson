from manager import db
import json

class OrderManager(db.Model):
    """docstring for OrderManager"""
    def __init__(self):
        super(OrderManager, self).__init__()
    
    @staticmethod
    def delete(ID):
        temp = OrderManager.query.filter(OrderManager.orderID == ID).first()
        # temp =  OrderManager(orderID = ID,orderName = Name,buyer = buyer2,seller= seller2,orderItems=Items,orderStatus = "Booking",orderTime = datetime.utcnow())
        db.session.delete(temp)
        db.session.commit()

    @staticmethod
    def insert(temp):
        db.session.add(temp)
        db.session.commit()
        

    @staticmethod
    def printTable():
        table = OrderManager.query.all()
        result = []
        for line in table:
            temp = {}
            temp['orderID'] = line.orderID
            temp['orderName'] = line.orderName
            temp['buyer'] = line.buyer
            temp['seller'] = line.seller
            temp['orderStatus'] = line.orderStatus
            temp['orderItems'] = line.orderItems
            temp['orderTime'] = line.orderTime.strftime("%A, %d. %B %Y %I:%M%p")
            result.append(temp)
        # print result
        return result
        # return table


            # ID = OrderManager.orderID
            # name = OrderManager.orderName
            # buyer = OrderManager.buyer
            # seller = OrderManager.seller
            # iterms = OrderManager.orderItems
            # status = OrderManager.orderStatus
            # time = OrderManager.orderTime
       
        # return ID+" "+name+" "+ buyer+" "+seller+" "+items+" "+status+" "+ time


    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    orderID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    orderName = db.Column(db.String(50), index = True)
    buyer = db.Column(db.String(20)) #, db.ForeignKey('Buyer.buyerID')
    seller = db.Column(db.String(20)) # , db.ForeignKey('Seller.sellerID')
    orderItems = db.Column(db.String(200), index = False)
    # buyer = db.Column(db.String(20), db.ForeignKey('Buyer.buyerID'))
    # seller = db.Column(db.String(20), db.ForeignKey('Seller.sellerID'))
    # buyer = db.relationship("Buyer", backref = 'buyer', lazy = 'dynamic')
    # seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
    orderStatus = db.Column(db.Integer, index = False)
    orderTime = db.Column(db.DateTime, index = False)


                 