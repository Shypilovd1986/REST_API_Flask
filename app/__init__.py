"""main module of application  where initialize object of class Flask"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec


app = Flask(__name__)

app.config.from_object(Config)

test_client = app.test_client()

jwt = JWTManager(app)

docs = FlaskApiSpec(app)
#
# docs.init_app(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='english learning',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()]
    ),
    'APISPEC_SWAGGER_URL': '/swagger/'
})

from app import routes
