"""REST Controller for User"""
from app.domain.user import User as Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA
from app.controller.generic_controller import generate_api

generate_api('user', 'User API', Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA)
