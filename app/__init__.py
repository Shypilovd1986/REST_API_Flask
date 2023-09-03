"""main module of application  where initialize object of class Flask"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config


app = Flask(__name__)
test_client = app.test_client()
jwt = JWTManager(app)

app.config.from_object(Config)

from app import routes
