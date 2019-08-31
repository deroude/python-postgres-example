"""
Setup the common variables
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restplus import Api
from app.config import RestConfig, DbConfig

APP = Flask(__name__)
APP.config.from_object(RestConfig)
APP.config.from_object(DbConfig)
DB = SQLAlchemy(APP)
MIGRATE = Migrate(APP, DB)
MA = Marshmallow(APP)
REST = Api(APP)
