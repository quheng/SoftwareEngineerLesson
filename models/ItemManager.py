from manager import db

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
