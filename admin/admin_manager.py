import admin_config
from admin_config import admin
from admin_config import MyModelView
from manager import db
# add models
from models import OrderManager
from models import Complaints

admin.add_view(MyModelView(OrderManager.OrderManager, db.session))
admin.add_view(MyModelView(Complaints.Complaints, db.session))
