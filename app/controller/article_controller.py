"""REST Controller for Article"""
from app.domain.article import Article as Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA
from app.controller.generic_controller import generate_api

generate_api('article', 'Article API', Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA)
