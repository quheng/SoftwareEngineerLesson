from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api

class GetUserID(Resource):
    "use to get user ID"
    @swagger.operation(
        notes = "use to get user ID",
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

class GetUserNickname(Resource):
    "use to get user nickname"
    @swagger.operation(
        notes = "use to get user nickname",
        nickname='get')
    def get(self, response):
        """
        Get a todo task
        """
        return "Tom", 200, {'Access-Control-Allow-Origin': '*'}
