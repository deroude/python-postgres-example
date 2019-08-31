"""REST Controller for User"""
from flask import Blueprint

USER = Blueprint('user', __name__)

@USER.route('/')
def get():
    "Get all Users"
    return "User"
