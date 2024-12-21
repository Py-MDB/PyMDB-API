import os
from flask import Blueprint, jsonify
from pymongo import MongoClient

routes = Blueprint('routes', __name__)

# MongoDB configuration
mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")

client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
db = client["pyapi-db"]

@routes.route('/')
def home():
    return jsonify({"message": "Welcome to the PyMDB API!"})

@routes.route('/data')
def get_data():
    data = db.your_collection_name.find()
    return jsonify([item for item in data])
