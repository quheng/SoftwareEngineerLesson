from manager import db


class CountManager(db.Model):
	"""docstring for CountManager"""
	def __init__(self, arg):
		super(CountManager, self).__init__()
		self.arg = arg

	@staticmethod
	def get_count():
		return CountManager.query.all()

	def __repr__(self):
		return '<Count %r>' % (self.countID)

	countID = db.Column(db.String(20), primary_key = True)
	countPassword = db.Column(db.String(20), index = False)
	countType = db.Column(db.Integer, index = False)
	countStatus = db.Column(db.Integer, index = False)
	countProperty = db.Column(db.Float, index = False)

				