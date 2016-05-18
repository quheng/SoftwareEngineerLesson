from manager import db

class Complaints(db.Model):
    """docstring for Complaints"""

    @staticmethod
    def delete(ID):
        temp = Complaints.query.filter(Complaints.orderID == ID).first()
        # temp =  Complaints(orderID = ID,orderName = Name,buyer = buyer2,seller= seller2,orderItems=Items,orderStatus = "Booking",orderTime = datetime.utcnow())
        db.session.delete(temp)
        db.session.commit()

    @staticmethod
    def insert(temp):
        db.session.add(temp)
        db.session.commit()
        

    @staticmethod
    def printTable():
        orderID = Complaints.orderID
        buyer = Complaints.buyer
        content = Complaints.content
        time = Complaints.complaintTime
        return orderID+" "+ buyer+" "+content+" "+ time

    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    orderID = db.Column(db.String(20), primary_key = True)
    content = db.Column(db.String(200), index = False)
    buyer = db.Column(db.String(20), index = False)
    # seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
    # orderStatus = db.Column(db.String(20), index = False)
    complaintTime = db.Column(db.DateTime, index = False)


                 