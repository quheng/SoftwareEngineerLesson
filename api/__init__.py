import sys
sys.path.append("..")
from manager import app
from flasgger import Swagger
from flask import Flask, jsonify, request
Swagger(app)
import complaint
import order

@app.route("/a2/api/test", methods=['POST'])
def GetComplaintList():
    """
    use to test connection
    ---
    tags:
      - test
    parameters:
      - name: para
        in: query
        type: integer
        description: parameters test
    responses:
      200:
        description: test
        schema:
          id: res
          properties:
            result:
              type: string
              description: The test
              default: 'test'
    """
    para = request.args.get('para')
    if para is None:
        para = request.form['para']
    return jsonify({"result": para})
