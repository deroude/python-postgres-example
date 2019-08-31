"""Generic REST API"""
from flask import jsonify, request
from flask_restplus import Resource
from app.setup import DB, REST


def generate_api(ns_name, ns_description, entity, record_list_schema, record_schema):
    """API generator"""

    ns = REST.namespace(ns_name, description=ns_description)

    @ns.route('/')
    class AllRecordsAPI(Resource):
        """API for collection"""

        def get(self):
            """Get all Records"""
            records = entity.query.all()
            result = record_list_schema.dump(records)
            return jsonify(result)

        def post(self):
            """Add new Record"""
            new_record = record_schema.load(request.json)
            DB.session.add(new_record)
            DB.session.commit()
            result = record_schema.dump(new_record)
            return jsonify(result)

    @ns.route('/<int:record_id>')
    class SingleRecordAPI(Resource):
        """API for single record manipulation"""

        def get(self, record_id):
            """GET single record by id"""
            record = entity.query.filter_by(id=record_id).first_or_404()
            result = record_schema.dump(record)
            return jsonify(result)

        def put(self, record_id):
            """UPDATE record"""
            record = entity.query.filter_by(id=record_id).first_or_404()
            record.update(record_schema.load(request.json()))
            DB.session.commit()
            result = record_schema.dump(record)
            return jsonify(result)

        def delete(self, record_id):
            """DELETE record"""
            record = entity.query.filter_by(id=record_id).first_or_404()
            DB.session.delete(record)
            DB.session.commit()
            return '', 204
