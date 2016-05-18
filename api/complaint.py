from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api
from flask import request
from flask.ext.restful import reqparse
from datetime import datetime
from manager import db
from models.ComplaintsManager import ComplaintsManager


testdata = """
'[{  "id": "SE000010325",   "time": "2016.3.24",  "user": "ZaneXiao",   "amount": 66.2,   "state": "NotDel",  "imgsrc": "http://img1.imgtn.bdimg.com/it/u=1371246895,4061054626&fm=206&gp=0.jpg"},\
{"id": "SE000010510","time": "2016.3.22","user": "EowinYe","amount": "99.8","state": "Delivery","imgsrc": "http://d.hiphotos.baidu.com/image/h%3D200/sign=201258cbcd80653864eaa313a7dca115/ca1349540923dd54e54f7aedd609b3de9c824873.jpg"}]'
"""

class getComplaintsList(Resource):
    """get the Complaints list from the userID"""

    @swagger.operation(
        notes = "get the Complaints list from the userID",
        nickname='list',
        parameters=[{
            "name": "userID",
            "description": "the userID of the Complaints list",
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



class insertComplaint(Resource):
    """docstring for insertComplaints"""
    
    @swagger.operation(
        notes = "insert an Complaints",
        nickname='list',
        parameters=[{
            "name": "ComplaintsID",
            "description": "insert Complaints ",
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
        parser.add_argument('complaintTime', type=str)
        args = parser.parse_args()
        # temp =  ComplaintsManager(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],ComplaintsStatus = "Booking",
        #         ComplaintsTime = datetime.utcnow())
        # print args['ID']
        if args['orderID']==None:
            abort(400, message="orderID doesn't exist")
        if args['content']==None:
            abort(400, message="content doesn't exist")
        if args['buyer']==None:
            abort(400, message="buyer doesn't exist")

        newComplaints = Complaints()
        newComplaints.ComplaintsID = args['orderID']
        newComplaints.ComplaintsName = args['content']
        newComplaints.buyer = args['buyer']
        newComplaints.ComplaintsTime = datetime.utcnow()
        try:
            Complaints.insert(newComplaints)
        except Exception, e:
            abort(400,message="Database error: {0}".format(e))
        
        return 'insert successful', 200


class delete(Resource):
    """docstring for insertComplaints"""
    
    @swagger.operation(
        notes = "insert an Complaints",
        nickname='list',
        parameters=[{
            "name": "ComplaintsID",
            "description": "insert Complaints ",
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
        parser.add_argument('Name', type=str)
        args = parser.parse_args()
        # temp =  ComplaintsManager(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],ComplaintsStatus = "Booking",
        #         ComplaintsTime = datetime.utcnow())
        # print args['ID']
        if args['Name']==None:
            abort(400, message="Name doesn't exist")

        newComplaints = Complaints()
        newComplaints.ComplaintsName = args['Name']
        newComplaints.ComplaintsTime = datetime.utcnow()
        try:
            Complaints.delete(args['ID'])
        except Exception, e:
            abort(400,message="delete failure")
        
        return 'delete successful', 200


class selectComplaints(object):
    """docstring for searchComplaints"""
    
    @staticmethod
    def select( ID):
        # ComplaintsManager.query.filter(ComplaintsManager.ComplaintsID == ComplaintsID).first()
        # return ComplaintsManager.query.filter(ComplaintsManager.ComplaintsID == id).all()
        return Complaints.query.all()
        # return ComplaintsManager.get_Complaints(ID)
        
        
        