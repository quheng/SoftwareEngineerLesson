from flask import Flask, request, jsonify
from datetime import datetime
from manager import db, app
from models.Complaints import Complaints
from flask.ext.restful import abort

@app.route("/a2/api/getcomplaintbystatus", methods=['GET'])
def GetComplaintByStatus():
    """
    use to get complaint list
    ---
    tags:
      - complaint
    responses:
      200:
        description: A single user item
        schema:
          id: return_test
          properties:
            result:
              type: string
              description: The test
              default: 'test'
    """
    res = Complaints.selectByStatus()
    try:
        res = Complaints.selectByStatus()
    except Exception, e:
        res = 0
    result = {}
    result["result"] = res
    return jsonify({"result": result})


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
    newComplaint.buyer = request.form['buyer']
    newComplaint.content = request.form['content']
    newComplaint.orderID = srequest.form['orderID']
    newComplaint.complaintTime = datetime.utcnow()
    newComplaint.status = 0
    try:
        Complaints.insertComplaints(newComplaint)
        res = 1
    except Exception, e:
        res = 0
    return jsonify({"result": res})
