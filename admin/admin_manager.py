import admin_config
from admin_config import admin
from admin_config import MyModelView
from manager import db
# add models
from models import user
# Customized User model admin
# class UserInfo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     key = db.Column(db.String(64), nullable=False)
#     value = db.Column(db.String(64))
#     user_id = db.Column(db.Integer(), db.ForeignKey(user.User.id))
#     user = db.relationship(user.User, backref='info')
#
#     def __unicode__(self):
#         return '%s - %s' % (self.key, self.value)

admin.add_view(MyModelView(user.User, db.session))
admin.add_view(MyModelView(Seller.Seller, db.session))
admin.add_view(MyModelView(Buyer.Buyer, db.session))
admin.add_view(MyModelView(OrderManager.OrderManager, db.session))
admin.add_view(MyModelView(ItemManager.ItemManager, db.session))
admin.add_view(MyModelView(CountManager.CountManager, db.session))

