from flask import Flask, request, jsonify
from datetime import datetime
from manager import db, app
from models.Complaints import Complaints
from flask.ext.restful import abort

# @app.route("/a2/api/getcomplaintlist", methods=['GET'])
# def GetComplaintList():
#     """
#     use to get complaint list
#     ---
#     tags:
#       - complaint
#     parameters:
#       - name: userID
#         in: query
#         type: integer
#         description: size of elements
#     responses:
#       200:
#         description: A single user item
#         schema:
#           id: return_test
#           properties:
#             result:
#               type: string
#               description: The test
#               default: 'test'
#     """
#     userID = request.args.get('userID')
#     return jsonify({"result": userID})


@app.route("/a2/api/newcomplaint", methods=['POST'])
def NewComplaint():
    """
    add new complaint
    ---
    tags:
      - complaint
    parameters:
      - name: buyer
        in: query
        type: integer
        description: buyer ID
      - name: content
        in: query
        type: string
        description: content of complaint
      - name: orderID
        in: query
        type: integer
        description: order id
    responses:
      200:
        description: add result
        schema:
          id: result
          properties:
            result:
              type: string
              description: The result, 1 is successful
              default: '1'
    """
    newComplaint = Complaints()
    newComplaint.buyer = request.args.get('buyer')
    newComplaint.content = request.args.get('content')
    newComplaint.orderID = request.args.get('orderID')
    newComplaint.complaintTime = datetime.utcnow()
    newComplaint.status = 0
    try:
        Complaints.insertComplaints(newComplaint)
        res = 1
    except Exception, e:
        res = 0
    return jsonify({"result": res})
