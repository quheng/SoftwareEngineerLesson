from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api
from flask import request
from flask.ext.restful import reqparse

testdata = """
'[{  "id": "SE000010325",   "time": "2016.3.24",  "user": "ZaneXiao",   "amount": 66.2,   "state": "NotDel",  "imgsrc": "http://img1.imgtn.bdimg.com/it/u=1371246895,4061054626&fm=206&gp=0.jpg"},\
{"id": "SE000010510","time": "2016.3.22","user": "EowinYe","amount": "99.8","state": "Delivery","imgsrc": "http://d.hiphotos.baidu.com/image/h%3D200/sign=201258cbcd80653864eaa313a7dca115/ca1349540923dd54e54f7aedd609b3de9c824873.jpg"}]'
"""

class getOrderList(Resource):
    """get the order list from the userID"""

    @swagger.operation(
        notes = "get the order list from the userID",
        nickname='list',
        parameters=[{
            "name": "userID",
            "description": "the userID of the order list",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "string"}],
        responseMessages=[{
            "code": 200,
            "message": "right message"
        }, {
            "code": 405,
            "message": "Invalid input"
        }])
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userID', type=str)
        args = parser.parse_args()
        # userID = int(max(TODOS.keys()).lstrip('todo')) + 1
        # userID = 'todo%i' % userID
        userID = {'userID': args['userID']}
        return testdata, 200
