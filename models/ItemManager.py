from manager import db

class ItemManager(db.Model):
	"""docstring for ItemManager"""

	@staticmethod
	def get_item():
		return ItemManager.query.all()

	def __repr__(self):
		return '<Count %r>' % (self.itemID)

	itemID = db.Column(db.String(20), primary_key = True)
	itemName = db.Column(db.String(50), index = True)
	seller = db.Column(db.String(20) )#, db.ForeignKey('Seller.sellerID'),
	# seller = db.relationship("Seller", backref = 'seller', lazy = 'dynamic')
	itemType = 	db.Column(db.Integer, index = False)
	itemStatus = db.Column(db.Integer, index = False)
