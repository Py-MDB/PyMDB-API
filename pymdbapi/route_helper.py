from flask import jsonify, request
from pymdbapi.mongodb import PyMongoDB
from pymdbapi.schema import DatabaseSchema
from cerberus import Validator


db = PyMongoDB()
schema = DatabaseSchema()


class RouteHelper:
    def __init__(self):
        pass

    def get_data(self, collection_name):
        filters = request.args.to_dict()
        includes = filters.pop('include', '').split(',')
        if filters:
            try:
                data = db.find_by_key_value(collection_name, filters, includes)
                if not data:
                    return jsonify({"error": "No data found"}), 404
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            try:
                data = db.get_all(collection_name, includes)
                if not data:
                    return jsonify([]), 200
                return jsonify(data), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
    def get_data_by_id(self, collection_name, id):
        filters = request.args.to_dict()
        includes = filters.pop('include', '').split(',')
        try:
            data = db.find_by_key_value(collection_name, {'id': id}, includes)
            if not data:
                return jsonify({"error": "No data found"}), 404
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    def add_data(self, collection_name):
        collection_schema = getattr(schema, f"{collection_name}_schema")
        validator = Validator(collection_schema)
        data = request.json
        if not validator.validate(data):
            return jsonify({"error": "Invalid data", "details": validator.errors}), 400
        inserted_id = db.insert(collection_name, data)
        return jsonify({"inserted_id": inserted_id}), 201
    
    def delete_data_by_id(self, collection_name, id):
        if id:
            try:
                deleted_count = db.delete_by_id(collection_name, id)
                if deleted_count == 0:
                    return jsonify({"error": "No data found to delete"}), 404
                return jsonify({"deleted_count": deleted_count}), 200
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            return jsonify({"error": "id parameter is required"}), 400
