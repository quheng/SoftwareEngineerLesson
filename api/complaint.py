from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api
from flask import request
from flask.ext.restful import reqparse
from datetime import datetime
from manager import db
from models.Complaints import Complaints


testdata = """
'[{  "id": "SE000010325",   "time": "2016.3.24",  "user": "ZaneXiao",   "amount": 66.2,   "state": "NotDel",  "imgsrc": "http://img1.imgtn.bdimg.com/it/u=1371246895,4061054626&fm=206&gp=0.jpg"},\
{"id": "SE000010510","time": "2016.3.22","user": "EowinYe","amount": "99.8","state": "Delivery","imgsrc": "http://d.hiphotos.baidu.com/image/h%3D200/sign=201258cbcd80653864eaa313a7dca115/ca1349540923dd54e54f7aedd609b3de9c824873.jpg"}]'
"""

class getcomplaintList(Resource):
    """get the complaint list from the userID"""

    @swagger.operation(
        notes = "get the complaint list from the userID",
        nickname='list',
        parameters=[{
            "name": "userID",
            "description": "the userID of the complaint list",
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
        return userID, 200



class insertcomplaint(Resource):
    """docstring for insertcomplaint"""
    
    @swagger.operation(
        notes = "insert an complaint",
        nickname='list',
        parameters=[{
            "name": "complaintID",
            "description": "insert complaint ",
            "required": True,
            "allowMultiple": False,
            "dataType": "string",
            "paramType": "string"}],
        responseMessages=[{
            "code": 200,
            "message": "right message"
        }, {
            "code": 400,
            "message": "Invalid input"
        }])

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderID', type=str)
        parser.add_argument('content', type=str)
        parser.add_argument('buyer', type=str)
        args = parser.parse_args()
        # temp =  Complaints(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],complaintStatus = "Booking",
        #         complaintTime = datetime.utcnow())
        # print args['ID']
        if args['orderID']==None:
            abort(400, message="ID doesn't exist")
        if args['content']==None:
            abort(400, message="Name doesn't exist")
        if args['buyer']==None:
            abort(400, message="buyer doesn't exist")
        newcomplaint = Complaints()
        newcomplaint.complaintID = args['orderID']
        newcomplaint.complaintName = args['content']
        newcomplaint.buyer = args['buyer']
        newcomplaint.complaintTime = datetime.utcnow()
        try:
            Complaints.insert(newcomplaint)
        except Exception, e:
            abort(400,message="Database error: {0}".format(e))
        
        return 'insert successful', 200


class deletecomplaint(Resource):
    """docstring for insertcomplaint"""
    
    @swagger.operation(
        notes = "insert an complaint",
        nickname='list',
        parameters=[{
            "name": "complaintID",
            "description": "insert complaint ",
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

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('orderID', type=str)
        args = parser.parse_args()
        # temp =  Complaints(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],complaintStatus = "Booking",
        #         complaintTime = datetime.utcnow())
        # print args['ID']
        if args['orderID']==None:
            abort(400, message="orderID doesn't exist")

        newcomplaint = Complaints()
        newcomplaint.complaintName = args['orderID']
        try:
            Complaints.delete(args['orderID'])
        except Exception, e:
            abort(400,message="delete failure")
        
        return 'delete successful', 200


class selectcomplaint(object):
    """docstring for searchcomplaint"""
    
    @staticmethod
    def select():
        # Complaints.query.filter(Complaints.complaintID == complaintID).first()
        # return Complaints.query.filter(Complaints.complaintID == id).all()
        return Complaints.query.all()
        # return Complaints.get_complaint(ID)
        
        
        