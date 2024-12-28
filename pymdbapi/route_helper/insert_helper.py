"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import jsonify, request
from pymdbapi.mongodb import PyMongoDB
from pymdbapi.schema import DatabaseSchema
from cerberus import Validator
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = PyMongoDB()
schema = DatabaseSchema()

def upsert_data(collection_name: str, id: str = None) -> tuple:
    """
    Add or modify data in a specified collection.

    Args:
        collection_name (str): The name of the collection to add or modify data in.
        id (str, optional): The unique ID of the document to modify. If None, a new document will be created.

    Returns:
        Response: A Flask response object containing the upserted ID or an error message.
    """
    collection_schema = getattr(schema, f"{collection_name}_schema")
    validator = Validator(collection_schema)
    new_data = request.json
    logger.info(f"New data: {new_data}")
    if id:
        try:
            current_data = db.find_by_key_value(collection_name, {'id': id})
            if not current_data:
                return jsonify({"error": "No data found to update"}), 404
            current_data[0].update(new_data)
            if not validator.validate(current_data[0]):
                logger.error(f"Validation errors: {validator.errors}")
                return jsonify({"error": "Invalid data", "details": validator.errors}), 400
            updated_count = db.update_by_id(collection_name, id, current_data[0])
            return jsonify({"updated_id": id}), 200
        except Exception as e:
            logger.error(f"Error updating data in {collection_name}: {e}")
            return jsonify({"error": "Internal Server Error"}), 500
    else:
        if not validator.validate(new_data):
            logger.error(f"Validation errors: {validator.errors}")
            return jsonify({"error": "Invalid data", "details": validator.errors}), 400
        try:
            inserted_id = db.insert(collection_name, new_data)
            return jsonify({"inserted_id": inserted_id}), 201
        except Exception as e:
            logger.error(f"Error inserting data into {collection_name}: {e}")
            return jsonify({"error": "Internal Server Error"}), 500
