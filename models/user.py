from manager import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    @staticmethod
    def get_users():
        return User.query.all()

    def __repr__(self):
        return '<User %r>' % (self.nickname)

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


class Buyer(db.Mode):
	"""docstring for Buyer"""

	def __init__(self, arg):
		super(Buyer, self).__init__()
		self.arg = arg

	def get_buyer():
		return Buyer.query.all()

	def __repr__(self):
        return '<Buyer %r>' % (self.buyerID)

	buyerID = db.Column(db.String(20), primary_key = True)
	buyerName = db.Column(db.String(50), index = True)
	buyerCount = db.relationship("CountManager", backref = 'count', lazy = 'dynamic', uselist = False)


class CountManager(db.Mode):
	"""docstring for CountManager"""
	def __init__(self, arg):
		super(CountManager, self).__init__()
		self.arg = arg

	def get_count():
		return CountManager.query.all()

	def __repr__(self):
		return '<Count %r>' % (self.countID)

	countID = db.Column(db.String(20), primary_key = True)
	countPassword = db.Column(db.String(20), primary_key = True)
	countType = db.Column(db.Integer, index = False)
	countStatus = db.Column(db.Integer, index = False)
	countProperty = db.Column(db.Float, index = False)

class ItemManager(db.Mode):
	"""docstring for ItemManager"""
	def __init__(self, arg):
		super(ItemManager, self).__init__()
		self.arg = arg

	def get_item():
		return ItemManager.query.all()

	def __repr__(self):
		return '<Count %r>' % (self.itemID)

	itemID = db.Column(db.String(20), primary_key = True)
	itemName = db.Column(db.String(50), index = True)
	seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
	itemType = 	db.Column(db.Integer, index = False)
	itemStatus = db.Column(db.Integer, index = False)
		
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


				