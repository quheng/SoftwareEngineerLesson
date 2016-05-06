from manager import db

class OrderManager(db.Mode):
	"""docstring for OrderManager"""
	def __init__(self, arg):
		super(OrderManager, self).__init__()
		self.arg = arg
	
	def get_order():
		return OrderManager.query.all()

	def __repr__(self):
		return '<Count %r>' % (self.orderID)

	orderID = db.Column(db.String(20), primary_key = True)
	orderName = db.Column(db.String(50), index = True)
	buyer = db.relationship("Buyer", backref = 'buyer', lazy = 'dynamic')
	seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
	orderStatus = db.Column(db.Integer, index = False)
	orderTime = db.Column(db.Time, index = False)


				