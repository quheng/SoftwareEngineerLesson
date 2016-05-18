from manager import db

class OrderManager(db.Model):
    """docstring for OrderManager"""

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
        ID = OrderManager.orderID
        name = OrderManager.orderName
        buyer = OrderManager.buyer
        seller = OrderManager.seller
        iterms = OrderManager.orderItems
        status = OrderManager.orderStatus
        time = OrderManager.orderTime
        return ID+" "+name+" "+ buyer+" "+seller+" "+items+" "+status+" "+ time

    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    orderID = db.Column(db.String(20), primary_key = True)
    orderName = db.Column(db.String(50), index = True)
    buyer = db.Column(db.String(20)) #, db.ForeignKey('Buyer.buyerID')
    seller = db.Column(db.String(20)) # , db.ForeignKey('Seller.sellerID')
    orderItems = db.Column(db.String(200), index = False)
    # buyer = db.relationship("Buyer", backref = 'buyer', lazy = 'dynamic')
    # seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
    orderStatus = db.Column(db.String(20), index = False)
    orderTime = db.Column(db.DateTime, index = False)


                 