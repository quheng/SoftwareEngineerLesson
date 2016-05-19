import sys
sys.path.append("..")
from manager import app
from flask_restful_swagger import swagger
from flask.ext.restful import Api

# This is important:
api = swagger.docs(Api(app), apiVersion='0.1', api_spec_url='/api/api')

import getuser
import getseller
import order
api.add_resource(getuser.GetUserID, '/a2/api/UserID')
api.add_resource(order.selectOrder, '/a2/api/selectOrder')
api.add_resource(order.deleteOrder, '/a2/api/deleteOrder')
api.add_resource(order.insertOrder, '/a2/api/insertOrder')
api.add_resource(order.selectOrderByID, '/a2/api/selectOrderBy')

# api.add_resource(getuser.GetUserNickname, '/api/nickname')
# api.add_resource(getseller.GetSellerID, '/api/SellerID')
api.add_resource(getuser.UpdateUserNickname, '/a2/api/update_nickname')
