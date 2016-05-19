from flask.ext.restful import reqparse, abort, Api, Resource, fields, marshal_with
from flask_restful_swagger import swagger
from api import api
from flask import request
from flask.ext.restful import reqparse
from datetime import datetime
from manager import db
import json
from models.OrderManager import OrderManager


testdata = """
'[{  "id": "SE000010325",   "time": "2016.3.24",  "user": "ZaneXiao",   "amount": 66.2,   "state": "NotDel",  "imgsrc": "http://img1.imgtn.bdimg.com/it/u=1371246895,4061054626&fm=206&gp=0.jpg"},\
{"id": "SE000010510","time": "2016.3.22","user": "EowinYe","amount": "99.8","state": "Delivery","imgsrc": "http://d.hiphotos.baidu.com/image/h%3D200/sign=201258cbcd80653864eaa313a7dca115/ca1349540923dd54e54f7aedd609b3de9c824873.jpg"}]'
"""


class insertOrder(Resource):
    """docstring for insertOrder"""
    
    @swagger.operation(
        notes = "insert an order",
        nickname='list',
        parameters=[{
            "name": "orderID",
            "description": "insert order ",
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
        parser.add_argument('ID', type=str)
        parser.add_argument('Name', type=str)
        parser.add_argument('buyer', type=str)
        parser.add_argument('seller', type=str)
        parser.add_argument('orderItems', type=str)
        args = parser.parse_args()
        # temp =  OrderManager(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],orderStatus = "Booking",
        #         orderTime = datetime.utcnow())
        # print args['ID']
        # if args['ID']==None:
            # abort(400, message="ID doesn't exist")
        if args['Name']==None:
            abort(400, message="Name doesn't exist")
        if args['buyer']==None:
            abort(400, message="buyer doesn't exist")
        if args['seller']==None:
            abort(400, message="seller doesn't exist")
        if args['orderItems']==None:
            abort(400, message="orderItems doesn't exist")

        newOrder = OrderManager()
        # newOrder.orderID = args['ID']
        newOrder.orderName = args['Name']
        newOrder.buyer = args['buyer']
        newOrder.seller = args['seller']
        newOrder.orderItems = args['orderItems']
        newOrder.orderStatus = 2
        newOrder.orderTime = datetime.utcnow()
        try:
            OrderManager.insert(newOrder)
        except Exception, e:
            abort(400,message="Database error: {0}".format(e))
        
        return 'insert successful', 200


class deleteOrder(Resource):
    """docstring for insertOrder"""
    
    @swagger.operation(
        notes = "delete an order",
        nickname='list',
        parameters=[{
            "name": "orderID",
            "description": "delete order ",
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
        # temp =  OrderManager(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],orderStatus = "Booking",
        #         orderTime = datetime.utcnow())
        # print args['ID']
        if args['Name']==None:
            abort(400, message="Name doesn't exist")

        newOrder = OrderManager()
        newOrder.orderName = args['Name']
        newOrder.orderTime = datetime.utcnow()
        try:
            OrderManager.delete(args['ID'])
        except Exception, e:
            abort(400,message="delete failure")
        
        return 'delete successful', 200


class selectOrder(Resource):
    """docstring for searchOrder"""
    
    @swagger.operation(
        notes = "select an order",
        nickname='list',
        parameters=[{
            "name": "orderID",
            "description": "select order ",
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
        # OrderManager.query.filter(OrderManager.orderID == orderID).first()
        # return OrderManager.query.filter(OrderManager.orderID == id).all()
        table = OrderManager.printTable()
        encodedjson = json.dumps(table)
        return encodedjson,200
        # return OrderManager.get_order(ID)
        

class selectOrderByID(Resource):
    """docstring for searchOrder"""
    
    @swagger.operation(
        notes = "select an order by ID",
        nickname='list',
        parameters=[{
            "name": "orderID",
            "description": "select order by ID",
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
        parser.add_argument('ID', type=str)
        args = parser.parse_args()
        # temp =  OrderManager(args['ID'],args['Name'],args['buyer'],
        #         args['seller'],args['Items'],orderStatus = "Booking",
        #         orderTime = datetime.utcnow())
        # print args['ID']
        if args['ID']==None:
            abort(400, message="ID doesn't exist")
            
        try:
            OrderManager.selectOrderByID(args['ID'])
        except Exception, e:
            abort(400,message="select failure")
        
        return 'select successful', 200
        
        