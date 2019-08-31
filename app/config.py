"""Configuration module"""
import os


class RestConfig(object):
    """Rest service config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'
    DEBUG = True
    CSRF_ENABLED = True


class DbConfig(object):
    """DB Config"""
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'postgresql+psycopg2://localhost'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
