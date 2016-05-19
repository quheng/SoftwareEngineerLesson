from manager import db


class Seller(db.Model):
	"""docstring for Seller"""

	def __init__(self):
		super(Seller, self).__init__()

	@staticmethod
	def get_seller():
		return Seller.query.all()

	def __repr__(self):
		return '<Seller %r>' % (self.sellerID)

	sellerID = db.Column(db.String(20), primary_key = True)
	sellerPhoto = db.Column(db.String(100))
	sellerName = db.Column(db.String(50), index = True)
	sellerCount = db.Column(db.String(20)) #, db.ForeignKey('CountManager.countID')
	# sellerCount = db.relationship("CountManager", backref = 'count', lazy = 'dynamic', uselist = False)
