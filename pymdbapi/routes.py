import os
from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from cerberus import Validator
from bson import ObjectId
from pymdbapi.schema import DatabaseSchema

schema = DatabaseSchema()
routes = Blueprint('routes', __name__)

# MongoDB configuration
mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
mongo_host = os.getenv("MONGO_HOST", "mongodb")
mongo_port = os.getenv("MONGO_PORT", 27017)

print(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/", flush=True)
client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client["pyapi-db"]

# Debugging connection
print(f"Connected to MongoDB at {mongo_host}:{mongo_port}", flush=True)

@routes.route('/')
def home():
    return jsonify({"message": "Welcome to the PyMDB API!"})

@routes.route('/hardware')
def get_data():
    try:
        data = list(db.hardware_data.find())
        print(f"Raw data from MongoDB: {data}", flush=True)  # Debugging line
        for item in data:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string
        print(f"Processed data: {data}", flush=True)  # Debugging line
        if not data:
            return jsonify([]), 200
        return jsonify(data), 200
    except Exception as e:
        print(f"Error retrieving data: {e}", flush=True)  # Debugging line
        return jsonify({"error": str(e)}), 500

validator = Validator(schema.hardware_schema)

@routes.route('/hardware', methods=['POST'])
def create_data():
    data = request.json
    if not validator.validate(data):
        return jsonify({"error": "Invalid data", "details": validator.errors}), 400
    result = db.hardware_data.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

