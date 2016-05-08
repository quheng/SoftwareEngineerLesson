from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api
from flask import request
from flask.ext.restful import reqparse

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
            "paramType": "body"}])


    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userID', type=str, required = True)
        args = parser.parse_args()
        # userID = int(max(TODOS.keys()).lstrip('todo')) + 1
        # userID = 'todo%i' % userID
        userID = {'userID': args['userID']}
        return userID, 200
