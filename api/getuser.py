from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api

class GetUserID(Resource):
    "use to get user ID"
    @swagger.operation(
        notes = "use to get user ID",
        nickname='post',
        parameters=[{
            "name": "body",
            "description": "A TODO item",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "string"}])
    def post(self):
        """
        this is show at line end
        """
        return "test id", 200, {'Access-Control-Allow-Origin': '*'}

class UpdateUserNickname(Resource):
    "update user nickname"
    @swagger.operation(
        notes = "update user nickname",
        nickname='put',
        parameters=[{
            "name": "update nickname",
            "description": "userID of you want to update",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "string"}, {
                "name": "new nickname",
                "description": "new nickname",
                "required": True,
                "allowMultiple": False,
                "dataType": "string",
                "paramType": "string"}])
    def put(self):
        """
        this is show at line end
        """
        return "", 200, {'Access-Control-Allow-Origin': '*'}

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
