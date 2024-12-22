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
def get_data():
    filters = request.args.to_dict()
    if filters:
        try:
            data = db.find_by_key_value('hardware_data', filters)
            if not data:
                return jsonify({"error": "No data found"}), 404
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        try:
            data = db.get_all('hardware_data')
            if not data:
                return jsonify([]), 200
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@routes.route('/hardware', methods=['POST'])
def create_data():
    validator = Validator(schema.hardware_schema)
    data = request.json
    if not validator.validate(data):
        return jsonify({"error": "Invalid data", "details": validator.errors}), 400
    inserted_id = db.insert('hardware_data', data)
    return jsonify({"inserted_id": inserted_id}), 201

@routes.route('/hardware', methods=['DELETE'])
def delete_data():
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

