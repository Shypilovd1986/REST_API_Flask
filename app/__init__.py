"""main module of application  where initialize object of class Flask"""
from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
test_client = app.test_client()
jwt = JWTManager(app)

from app import routes
