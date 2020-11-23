from flask import Flask
from core.router import Router
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/uploads/": {"origins": "*"}})
Router.run(app)