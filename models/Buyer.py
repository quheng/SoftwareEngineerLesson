from manager import db


class Buyer(db.Model):
	"""docstring for Buyer"""

	def __init__(self, arg):
		super(Buyer, self).__init__()
		self.arg = arg

	@staticmethod
	def get_buyer():
		return Buyer.query.all()

	def __repr__(self):
		return '<Buyer %r>' % (self.buyerID)

	buyerID = db.Column(db.String(20), primary_key = True)
	buyerName = db.Column(db.String(50), index = True)
	buyerCount = db.relationship("CountManager", backref = 'count', lazy = 'dynamic', uselist = False)
