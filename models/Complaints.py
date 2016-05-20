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
    def insertComplaints(newComplaint):
        newComplaint.complaintTime
        db.session.add(newComplaint)
        db.session.commit()

    @staticmethod
    def selectByOrderID(ID):
        temp = Complaints.query.filter(Complaints.orderID == ID).first()
        result = {}
        result['orderID'] = Complaints.orderID
        result['content'] = Complaints.content
        result['buyer'] = Complaints.buyer
        result['complaintTime'] = Complaints.orderTime.strftime("%A, %d. %B %Y %I:%M%p")
        return result

    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    complaintID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    orderID = db.Column(db.Integer)
    content = db.Column(db.String(200))
    buyer = db.Column(db.Integer)
    status = db.Column(db.Integer)
    complaintTime = db.Column(db.DateTime)
