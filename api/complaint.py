from flask import Flask, request
from datetime import datetime
from manager import db, app
from models.Complaints import Complaints
from flask.ext.restful import abort

@app.route("/a2/api/getcomplaintlist", methods=['GET'])
def GetComplaintList():
    """
    use to get complaint list
    ---
    tags:
      - complaint
    parameters:
      - name: userID
        in: query
        type: integer
        description: size of elements
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
    userID = request.args.get('userID')
    return jsonify({"result": userID})
