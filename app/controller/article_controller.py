"""REST Controller for Article"""
from flask import jsonify, request
from flask_restplus import Resource
from app.domain.article import Article as Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA
# from app.controller.generic_controller import generate_api
from app.setup import REST, DB

# generate_api('article', 'Article API', Entity, RECORD_LIST_SCHEMA, RECORD_SCHEMA)

ns = REST.namespace('article', description='Article API')

@ns.route('/')
class AllRecordsAPI(Resource):
    """API for collection"""

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

@ns.route('/<int:record_id>')
class SingleRecordAPI(Resource):
    """API for single record manipulation"""

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
