from flask import Flask, request, jsonify
from datetime import datetime
from manager import db, app
from models.OrderManager import OrderManager
from flask.ext.restful import abort
from models.OrderManager import OrderCondition

@app.route("/a2/api/updateorderstate", methods=['POST'])
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
              description: The result, 1 is successful
              default: '1'
    """
    orderJson = request.get_json()

    orderID = orderJson['orderID']
    status = orderJson['status']
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
              description: The result, 1 is successful
              default: '1'
    """
    newOrder = OrderManager()
    newOrder.buyer = request.form['buyer']
    newOrder.seller = request.form['seller']
    newOrder.orderAmount = request.form['orderAmount']
    newOrder.orderItems = request.form['orderItems']
    newOrder.orderStatus = request.form['orderStatus']
    data = request.form['orderTime']
    newOrder.orderTime = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

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
    if orderID is None:
        abort(400, message="you should pass order id")
    try:
        res = OrderManager.selectOrderByID(orderID)
    except Exception, e:
        abort(400, message="Database error: {0}".format(e))
    return jsonify(res)

@app.route("/a2/api/getorderlist", methods=['GET'])
def GetOrderList():
    """
    use to get orders list of one user
    ---
    tags:
      - order
    parameters:
      - name: userID
        in: query
        type: integer
        description: user ID
    responses:
      200:
        description: order list
        schema:
          id: return_test
          properties:
            orderIdList:
              type: Integer
              description: order id list
              default: 'a json array'
    """
    userID = request.args.get('userID')
    if userID is None:
        abort(400, message="you should pass order id")
    try:
        res = OrderManager.selectOrderByUser(userID)
    except Exception, e:
        abort(400, message="Database error: {0}".format(e))
    result = {}
    result["orderIdList"] = res
    return jsonify(result)

@app.route("/a2/api/getorderlistbydate", methods=['GET'])
def GetOrderListByDate():
    """
    use to get orders list by date
    ---
    tags:
      - order
    parameters:
      - name: start
        in: query
        type: string
        description: start time
      - name: end
        in: query
        type: string
        description: end time
    responses:
      200:
        description: order list
        schema:
          id: return_test
          properties:
            orderIdList:
              type: Integer
              description: order id list
              default: 'a json array'
    """
    start = request.args.get('start')
    start = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end = request.args.get('end')
    end = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    if start is None:
        abort(400, message="you should pass order id")
    try:
        res = OrderManager.getOrderListByDate(start, end)
    except Exception, e:
        abort(400, message="Database error: {0}".format(e))
    result = {}
    result["orderIdList"] = res
    return jsonify(result)


@app.route("/a2/api/getallorder", methods=['GET'])
def getAllOrder():
    """
    use to get all orders details of one user
    ---
    tags:
      - order
    parameters:
      - name: userID
        in: query
        type: integer
        description: user ID
    responses:
      200:
        description: order list
        schema:
          id: return_test
          properties:
            orderIdList:
              type: json array
              description: order details list
              default: 'a json array'
    """
    userID = request.args.get('userID')
    res = OrderManager.selectAllOrder(userID)
    if userID is None:
        abort(400, message="you should pass order id")
    try:
        res = OrderManager.selectAllOrder(userID)
    except Exception, e:
        abort(400, message="Database error: {0}".format(e))
    result = {}
    result["orderDetailList"] = res
    return jsonify(result)


@app.route("/a2/api/getorder", methods=['GET'])
def GetOrders():
    """
    use to get orders list by condition
    ---
    tags:
      - order
    parameters:
      - name: userID
        in: query
        type: integer
        description: user ID
      - name: date
        in: query
        type: integer
        description: date
      - name: status
        in: query
        type: integer
        description: status
      - name: sort
        in: query
        type: integer
        description: sort
    responses:
      200:
        description: order list
        schema:
          id: return_test
          properties:
            orderIdList:
              type: Integer
              description: order id list
              default: 'a json array'
    """

    condition = OrderCondition()
    condition.userID = request.args.get('userID')
    if condition.userID is None:
        abort(400, message="you should pass order id")
    condition.date = request.args.get('date')
    if condition.date is None:
        abort(400, message="you should pass order date")
    condition.status = request.args.get('status')
    if condition.status is None:
        abort(400, message="you should pass status")
    condition.sort = request.args.get('sort')
    if condition.sort is None:
        abort(400, message="you should pass sort")

    res = OrderManager.selectOrderByCondition(condition)
    # try:
    #     res = OrderManager.selectOrderByCondition(condition)
    # except Exception, e:
    #     abort(400, message="Database error: {0}".format(e))
    result = {}
    result["orderIdList"] = res
    return jsonify(result)
