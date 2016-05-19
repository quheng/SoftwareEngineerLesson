import sys
sys.path.append("..")
from manager import app
from flasgger import Swagger
from flask import Flask, jsonify, request
Swagger(app)
import complaint
import order
