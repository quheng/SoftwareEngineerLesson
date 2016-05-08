from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api

class GetSellerID(Resource):
    "use to get seller ID"
    @swagger.operation(
        notes = "use to get seller ID",
        nickname='get',
        parameters=[{
            "name": "body",
            "description": "A TODO item",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "body"}])
    def get(self):
        """
        this is show at line end
        """
        return "test id", 200, {'Access-Control-Allow-Origin': '*'}

class GetSellerName(Resource):
    "use to get seller name"
    @swagger.operation(
        notes = "use to get seller name",
        nickname='get')

    def get(self, response):
        """
        Get a todo task
        """
        return "Tom", 200, {'Access-Control-Allow-Origin': '*'}

class GetSellerCount(Resource):
    "use to get seller count ID"
    @swagger.operation(
        notes = "use to get seller count ID",
        nickname='get')
    def get(self, response):
        """
        Get a todo task
        """
        return "Tom", 200, {'Access-Control-Allow-Origin': '*'}