from flask import Flask
from config import RestConfig, DbConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

api = Flask(__name__)
api.config.from_object(RestConfig)
api.config.from_object(DbConfig)
db = SQLAlchemy(api)
migrate = Migrate(api,db)