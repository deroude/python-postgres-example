"""Main module"""
import werkzeug
from app.setup import APP
# pylint:disable=wildcard-import
from app.controller import *


@APP.errorhandler(werkzeug.exceptions.NotFound)
# pylint:disable=unused-argument
def not_found(error):
    """Handler for 404"""
    return "Requested resource was not found"


if __name__ == "__main__":
    # Only for debugging while developing
    APP.run(host='0.0.0.0', debug=True, port=80)
