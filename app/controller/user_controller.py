"""REST Controller for User"""
from flask import request
from flask_restplus import Resource, fields
from flask_jwt import jwt_required
from passlib.hash import bcrypt
from app.domain.user import User as Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA
from app.setup import REST, DB


NS = REST.namespace('user', description='User API')

FIELDS = NS.model(
    'User', {
        'id': fields.Integer,
        'full_name': fields.String,
        'email': fields.String,
        'status': fields.String,
        'role': fields.String
    })


@NS.route('/')
class AllRecordsAPI(Resource):
    """API for collection"""
    @NS.marshal_list_with(FIELDS)
    @jwt_required()
    def get(self):
        """Get all Records"""
        records = Entity.query.all()
        return RECORD_LIST_SCHEMA.dump(records), 200

    @NS.marshal_with(FIELDS)
    @NS.doc(body=FIELDS)
    def post(self):
        """Add new Record"""
        new_record = RECORD_SCHEMA.load(request.json)
        new_record.password = bcrypt.hash(new_record.password)
        DB.session.add(new_record)
        DB.session.commit()
        return RECORD_SCHEMA.dump(new_record), 201


@NS.route('/<int:record_id>')
class SingleRecordAPI(Resource):
    """API for single record manipulation"""

    @NS.marshal_with(FIELDS)
    def get(self, record_id):
        """GET single record by id"""
        record = Entity.query.filter_by(id=record_id).first_or_404()
        return RECORD_SCHEMA.dump(record), 200

    @NS.marshal_with(FIELDS)
    def put(self, record_id):
        """UPDATE record"""
        record = Entity.query.filter_by(id=record_id).first_or_404()
        record.update(RECORD_SCHEMA.load(request.json()))
        DB.session.commit()
        return RECORD_SCHEMA.dump(record), 200

    def delete(self, record_id):
        """DELETE record"""
        record = Entity.query.filter_by(id=record_id).first_or_404()
        DB.session.delete(record)
        DB.session.commit()
        return '', 204
