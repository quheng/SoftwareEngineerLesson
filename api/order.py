from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api
from flask import request

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
            "paramType": "string"}])

    def get(self):
        return "test", 200, {'Access-Control-Allow-Origin': '*'}

        # return request.form['userID'], 200, {'Access-Control-Allow-Origin': '*'}
