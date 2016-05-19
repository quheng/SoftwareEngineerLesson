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

# @app.route("/a2/api/getorderdetial", methods=['GET'])
# def GetOrderDetial():
#     """
#     use to get orders detial by orderID
#     ---
#     tags:
#       - order
#     parameters:
#       - name: orderID
#         in: query
#         type: integer
#         description: size of elements
#     responses:
#       200:
#         description: order detail
#         schema:
#           id: return_test
#           properties:
#             buyer:
#               type: Integer
#               description: buyerId
#               default: '1'
#             orderTime:
#               type: String
#               description: the order time
#               default: '2016-05-02 19:11:00'
#     """
#     orderID = request.args.get('orderID')
#     print abort
#     if orderID is None:
#         abort(400, message="you should pass order id")
#     try:
#         res = OrderManager.selectOrderByID(orderID)
#     except Exception, e:
#         abort(400, message="Database error: {0}".format(e))
#     return jsonify(res)

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
              type: String
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
