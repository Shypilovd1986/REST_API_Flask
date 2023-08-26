"""main module of application  where initialize object of class Flask"""
from flask import Flask

app = Flask(__name__)
test_client = app.test_client()

from app import routes
