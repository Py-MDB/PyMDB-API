import os
from flask import Blueprint, jsonify, request
from cerberus import Validator
from pymdbapi.schema import DatabaseSchema
from pymdbapi.mongodb import PyMongoDB

schema = DatabaseSchema()
routes = Blueprint('routes', __name__)
db = PyMongoDB()

@routes.route('/')
def home():
    return jsonify({"message": "Welcome to the PyMDB API!"})

@routes.route('/hardware', methods=['GET'])
def get_hardware():
    filters = request.args.to_dict()
    includes = filters.pop('include', '').split(',')
    print(f"filters: {filters}", flush=True)
    print(f"includes: {includes}", flush=True)
    if filters:
        try:
            data = db.find_by_key_value('hardware_data', filters, includes)
            if not data:
                return jsonify({"error": "No data found"}), 404
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        try:
            data = db.get_all('hardware_data', includes)
            if not data:
                return jsonify([]), 200
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@routes.route('/hardware/<id>', methods=['GET'])
def get_hardware_by_id(id):
    try:
        data = db.find_by_key_value('hardware_data', {'id': id})
        if not data:
            return jsonify({"error": "No data found"}), 404
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route('/hardware', methods=['POST'])
def create_hardware():
    validator = Validator(schema.hardware_schema)
    data = request.json
    if not validator.validate(data):
        return jsonify({"error": "Invalid data", "details": validator.errors}), 400
    inserted_id = db.insert('hardware_data', data)
    return jsonify({"inserted_id": inserted_id}), 201

@routes.route('/hardware', methods=['DELETE'])
def delete_hardware():
    id = request.args.get('id')
    if id:
        try:
            deleted_count = db.delete_by_id('hardware_data', id)
            if deleted_count == 0:
                return jsonify({"error": "No data found to delete"}), 404
            return jsonify({"deleted_count": deleted_count}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "id parameter is required"}), 400

@routes.route('/facilities', methods=['GET'])
def get_facilities():
    filters = request.args.to_dict()
    includes = filters.pop('include', '').split(',')
    if filters:
        try:
            data = db.find_by_key_value('facilities', filters, includes)
            if not data:
                return jsonify({"error": "No data found"}), 404
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        try:
            data = db.get_all('facilities', includes)
            if not data:
                return jsonify([]), 200
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@routes.route('/facilities/<id>', methods=['GET'])
def get_facility_by_id(id):
    try:
        data = db.find_by_key_value('facilities', {'id': id})
        if not data:
            return jsonify({"error": "No data found"}), 404
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route('/facilities', methods=['POST'])
def create_facility():
    validator = Validator(schema.facilities_schema)
    data = request.json
    if not validator.validate(data):
        return jsonify({"error": "Invalid data", "details": validator.errors}), 400
    inserted_id = db.insert('facilities', data)
    return jsonify({"inserted_id": inserted_id}), 201

@routes.route('/facilities', methods=['DELETE'])
def delete_facility():
    id = request.args.get('id')
    if id:
        try:
            deleted_count = db.delete_by_id('facilities', id)
            if deleted_count == 0:
                return jsonify({"error": "No data found to delete"}), 404
            return jsonify({"deleted_count": deleted_count}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "id parameter is required"}), 400

@routes.route('/operating_systems', methods=['GET'])
def get_operating_systems():
    filters = request.args.to_dict()
    includes = filters.pop('include', '').split(',')
    if filters:
        try:
            data = db.find_by_key_value('operating_systems', filters, includes)
            if not data:
                return jsonify({"error": "No data found"}), 404
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        try:
            data = db.get_all('operating_systems', includes)
            if not data:
                return jsonify([]), 200
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@routes.route('/operating_systems/<id>', methods=['GET'])
def get_operating_system_by_id(id):
    try:
        data = db.find_by_key_value('operating_systems', {'id': id})
        if not data:
            return jsonify({"error": "No data found"}), 404
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@routes.route('/operating_systems', methods=['POST'])
def create_operating_system():
    validator = Validator(schema.operating_systems_schema)
    data = request.json
    if not validator.validate(data):
        return jsonify({"error": "Invalid data", "details": validator.errors}), 400
    inserted_id = db.insert('operating_systems', data)
    return jsonify({"inserted_id": inserted_id}), 201

@routes.route('/operating_systems', methods=['DELETE'])
def delete_operating_system():
    id = request.args.get('id')
    if id:
        try:
            deleted_count = db.delete_by_id('operating_systems', id)
            if deleted_count == 0:
                return jsonify({"error": "No data found to delete"}), 404
            return jsonify({"deleted_count": deleted_count}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "id parameter is required"}), 400

