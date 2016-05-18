from manager import db

class OrderManager(db.Model):
    """docstring for OrderManager"""
<<<<<<< HEAD
    def __init__(self):
        super(OrderManager, self).__init__()
    
=======

>>>>>>> 100d09621ed63309893bfc34cfb754e58d933613
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

<<<<<<< HEAD

=======
>>>>>>> 100d09621ed63309893bfc34cfb754e58d933613
    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    orderID = db.Column(db.String(20), primary_key = True)
    orderName = db.Column(db.String(50), index = True)
    buyer = db.Column(db.String(20)) #, db.ForeignKey('Buyer.buyerID')
    seller = db.Column(db.String(20)) # , db.ForeignKey('Seller.sellerID')
    orderItems = db.Column(db.String(200), index = False)
<<<<<<< HEAD
    # buyer = db.Column(db.String(20), db.ForeignKey('Buyer.buyerID'))
    # seller = db.Column(db.String(20), db.ForeignKey('Seller.sellerID'))
    # buyer = db.relationship("Buyer", backref = 'buyer', lazy = 'dynamic')
    # seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
    orderStatus = db.Column(db.Integer, index = False)
    orderTime = db.Column(db.Time, index = False)
=======
    # buyer = db.relationship("Buyer", backref = 'buyer', lazy = 'dynamic')
    # seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
    orderStatus = db.Column(db.String(20), index = False)
    orderTime = db.Column(db.DateTime, index = False)
>>>>>>> 100d09621ed63309893bfc34cfb754e58d933613


                 