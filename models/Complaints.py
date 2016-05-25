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
    def GetComplaintStatus(ID):
        temp = Complaints.query.filter(Complaints.complaintID == ID).one()
        res = {}
        res["status"] = temp.status
        return res

    @staticmethod
    def updateComplaints(ID, status):
        db.session.query(Complaints).filter(Complaints.complaintID == ID).update({Complaints.status: status})
        db.session.commit()
        return 1

    @staticmethod
    def selectByStatus():
        temp = Complaints.query.filter(Complaints.status == 0).all()
        res = []
        for item in temp:
            result = {}
            result['complaintID'] = item.complaintID
            result['orderID'] = item.orderID
            result['content'] = item.content
            result['buyer'] = item.buyer
            result['status'] = item.status
            result['complaintTime'] = item.complaintTime.strftime("%Y-%m-%d %H:%M:%S")
            res.append(result)
        return res

    def __repr__(self):
        return '<Count %r>' % (self.orderID)

    complaintID = db.Column(db.Integer, primary_key = True, autoincrement=True)
    orderID = db.Column(db.Integer)
    content = db.Column(db.String(200))
    buyer = db.Column(db.Integer)
    status = db.Column(db.Integer)
    complaintTime = db.Column(db.DateTime)
