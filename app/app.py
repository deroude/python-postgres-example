"""Main module"""
import werkzeug
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import RestConfig, DbConfig
from .controller import ARTICLE as ARTCLE_CONTROLLER, USER as USER_CONTROLLER

API = Flask(__name__)
API.config.from_object(RestConfig)
API.config.from_object(DbConfig)
DB = SQLAlchemy(API)
MIGRATE = Migrate(API, DB)

API.register_blueprint(ARTCLE_CONTROLLER, url_prefix="/article")
API.register_blueprint(USER_CONTROLLER, url_prefix="/user")

@API.errorhandler(werkzeug.exceptions.NotFound)
#pylint:disable=unused-argument
def not_found(error):
    """Handler for 404"""
    return "Requested resource was not found"


if __name__ == "__main__":
    # Only for debugging while developing
    API.run(host='0.0.0.0', debug=True, port=80)
