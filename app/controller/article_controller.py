"""REST Controller for Article"""
from flask import Blueprint

ARTICLE = Blueprint('article', __name__)

@ARTICLE.route('/')
def get():
    "Get all Articles"
    return "Article"
