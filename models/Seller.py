from manager import db


class Seller(db.Mode):
	"""docstring for Seller"""

	def __init__(self, arg):
		super(Seller, self).__init__()
		self.arg = arg

	def get_seller():
		return Seller.query.all()

	def __repr__(self):
        return '<Seller %r>' % (self.sellerID)

	sellerID = db.Column(db.String(20), primary_key = True)
	sellerName = db.Column(db.String(50), index = True)
	sellerCount = db.relationship("CountManager", backref = 'count', lazy = 'dynamic', uselist = False)
