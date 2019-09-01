"""Main module"""
import werkzeug
from flask_jwt import JWT
from passlib.hash import bcrypt
from app.setup import APP
# pylint:disable=wildcard-import
from app.controller import *

# Authorization section
from app.domain.user import User, UserStatus


def authenticate(username, password):
    """Method used by Flask JWT to perform authentication"""
    user = User.query.filter_by(email=username).first()
    if user and user.status == UserStatus.ACTIVE and bcrypt.verify(password, user.password):
        return user


def identity(payload):
    """Method used by Flask JWT to provide the authenticated user"""
    user_id = payload['identity']
    return User.query.filter_by(id=user_id).first()


JWT_AUTH = JWT(APP, authenticate, identity)


@APP.errorhandler(werkzeug.exceptions.NotFound)
# pylint:disable=unused-argument
def not_found(error):
    """Handler for 404"""
    return "Requested resource was not found"


if __name__ == "__main__":
    # Only for debugging while developing
    APP.run(host='0.0.0.0', debug=True, port=80)
