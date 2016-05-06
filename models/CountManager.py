from manager import db


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

				