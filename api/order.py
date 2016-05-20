from flask import Flask, request, jsonify
from datetime import datetime
from manager import db, app
from models.OrderManager import OrderManager
from flask.ext.restful import abort

@app.route("/a2/api/updateorderstate", methods=['PUT'])
def UpdateOrderState():
    """
    use to update orders state
    ---
    tags:
      - order
    parameters:
      - name: orderID
        in: query
        type: integer
        description: order id
      - name: status
        in: query
        type: integer
        description: new status
    responses:
      200:
        description: update result
        schema:
          id: result
          properties:
            result:
              type: string
              description: The result
              default: '1'
    """
    orderID = request.args.get('orderID')
    status = request.args.get('status')
    if orderID is None:
        abort(400, message="you should pass order id")
    if status is None:
        abort(400, message="you should pass status")
    try:
        res = OrderManager.UpdateOrderState(orderID, status)
        res = 1
    except Exception, e:
        res = 0
    return jsonify({'result': res})

@app.route("/a2/api/insertorder", methods=['POST'])
def InsertOrder():
    """
    use to insert a new order
    ---
    tags:
      - order
    parameters:
      - name: buyer
        in: query
        type: integer
        description: buyerId
      - name: seller
        in: query
        type: integer
        description: sellerId
      - name: orderAmount
        in: query
        type: integer
        description: the order total amount
      - name: orderItems
        in: query
        type: string
        description:  You should post a json string like {\"items\" [ 1, 2,3,4 ]}, note, there should be a colon between items and [1,2,3,4]
      - name: orderStatus
        in: query
        type: integer
        description:  order status
      - name: orderTime
        in: query
        type: string
        description:  format %Y %m %d %H %M %S
    responses:
      200:
        description: insert result
        schema:
          id: result
          properties:
            result:
              type: string
              description: The result
              default: '1'
    """
    newOrder = OrderManager()
    newOrder.buyer = request.args.get('buyer')
    newOrder.seller = request.args.get('seller')
    newOrder.orderAmount = request.args.get('orderAmount')
    newOrder.orderItems = request.args.get('orderItems')
    newOrder.orderStatus = request.args.get('orderStatus')
    data = request.args.get('orderTime')
    newOrder.orderTime = datetime.strptime(data, "%Y %m %d %H %M %S")

    if newOrder.buyer is None:
        abort(400, message="you should pass enough order")
    if newOrder.seller is None:
        abort(400, message="you should pass enough order")
    if newOrder.orderAmount is None:
        abort(400, message="you should pass enough order")
    if newOrder.orderItems is None:
        abort(400, message="you should pass enough order")
    if newOrder.orderStatus is None:
        abort(400, message="you should pass enough order")
    if newOrder.orderTime is None:
        abort(400, message="you should pass enough order")
    try:
        res = OrderManager.insertOrder(newOrder)
        res = 1
    except Exception, e:
        res = 0
    return jsonify({'result': res})

@app.route("/a2/api/getorderdetial", methods=['GET'])
def GetOrderDetial():
    """
    use to get orders detial
    ---
    tags:
      - order
    parameters:
      - name: orderID
        in: query
        type: integer
        description: order ID
    responses:
      200:
        description: order detail
        schema:
          id: return_test
          properties:
            buyer:
              type: Integer
              description: buyerId
              default: '1'
            seller:
              type: Integer
              description: sellerId
              default: '1'
            orderAmount:
              type: Float
              description: the total amount
              default: '0'
            orderItems:
              type: String
              description: the total order items
              default: '{"items": [ 1, 2,3,4 ]}'
            orderStatus:
              type: Integer
              description: the order status
              default: '0'
            orderTime:
              type: String
              description: the order time
              default: '2016-05-02 19:11:00'
    """
    orderID = request.args.get('orderID')
    print abort
    if orderID is None:
        abort(400, message="you should pass order id")
    try:
        res = OrderManager.selectOrderByID(orderID)
    except Exception, e:
        abort(400, message="Database error: {0}".format(e))
    return jsonify(res)
