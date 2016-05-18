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
api.add_resource(getuser.GetUserID, '/api/UserID')
# api.add_resource(getuser.GetUserNickname, '/api/nickname')
# api.add_resource(getseller.GetSellerID, '/api/SellerID')
api.add_resource(getuser.UpdateUserNickname, '/api/update_nickname')
api.add_resource(order.getOrderList, '/api/getOrderList')
