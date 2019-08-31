"""REST Controller for User"""
from flask import jsonify, request
from flask_restful import Resource
from app.domain.user import User as Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA
from app.setup import REST, DB


class AllRecordAPI(Resource):
    """API for /user"""

    def get(self):
        """Get all Records"""
        records = Entity.query.all()
        result = RECORD_LIST_SCHEMA.dump(records)
        return jsonify(result)

    def post(self):
        """Add new Record"""
        new_record = RECORD_SCHEMA.load(request.json)
        DB.session.add(new_record)
        DB.session.commit()
        result = RECORD_SCHEMA.dump(new_record)
        return jsonify(result)


class SingleRecordAPI(Resource):
    """API for /user/:id"""

    def get(self, record_id):
        """GET single record by id"""
        record = Entity.query.filter_by(id=record_id).first_or_404()
        result = RECORD_SCHEMA.dump(record)
        return jsonify(result)

    def put(self, record_id):
        """UPDATE record"""
        record = Entity.query.filter_by(id=record_id).first_or_404()
        record.update(RECORD_SCHEMA.load(request.json()))
        DB.session.commit()
        result = RECORD_SCHEMA.dump(record)
        return jsonify(result)

    def delete(self, record_id):
        """DELETE record"""
        record = Entity.query.filter_by(id=record_id).first_or_404()
        DB.session.delete(record)
        DB.session.commit()
        return '', 204


REST.add_resource(AllRecordAPI, '/user', endpoint="all_users")
REST.add_resource(SingleRecordAPI, '/user/<int:record_id>',
                  endpoint="user_by_id")
