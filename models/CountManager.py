from manager import db


class CountManager(db.Model):
	"""docstring for CountManager"""

	@staticmethod
	def get_count():
		return CountManager.query.all()

	@staticmethod
	def searchByID(countID):
		CountManager.query.filter(CountManager.name == countID).first()

	def __repr__(self):
		return '<Count %r>' % (self.countID)

	countID = db.Column(db.String(20), primary_key = True)
	countPassword = db.Column(db.String(20), index = False)
	countType = db.Column(db.String(20), index = False)
	countStatus = db.Column(db.String(20), index = False)
	countAmount = db.Column(db.Float, index = False)

				