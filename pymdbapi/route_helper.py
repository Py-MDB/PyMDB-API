"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import jsonify, request, url_for
from pymdbapi.mongodb import PyMongoDB
from pymdbapi.schema import DatabaseSchema
from cerberus import Validator
import uuid
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = PyMongoDB()
schema = DatabaseSchema()


class RouteHelper:
    def __init__(self):
        pass

    def get_data(self, collection_name: str) -> tuple:
        """
        Retrieve data from a specified collection with optional filters and includes.

        Args:
            collection_name (str): The name of the collection to retrieve data from.

        Returns:
            Response: A Flask response object containing the retrieved data or an error message.
        """
        filters = request.args.to_dict()
        includes = filters.pop('include', '').split(',')
        page = int(filters.pop('page', 1))
        limit = int(filters.pop('limit', 10))
        skip = (page - 1) * limit

        if filters:
            try:
                data = db.find_by_key_value(collection_name, filters, includes)
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        else:
            try:
                data = db.get_all(collection_name, includes)
            except Exception as e:
                return jsonify({"error": str(e)}), 500

        total_results = len(data)
        total_pages = (total_results + limit - 1) // limit
        paginated_data = data[skip:skip + limit]

        if not paginated_data:
            return jsonify({"error": "No data found"}), 404

        next_page = page + 1 if page < total_pages else None
        next_page_url = url_for(request.endpoint, page=next_page, limit=limit, _external=True) if next_page else None

        response = {
            collection_name: paginated_data,
            "meta": {
                "page": page,
                "total_pages": total_pages,
                "total_results": total_results,
                "next_page_url": next_page_url,
            },
        }

        return jsonify(response), 200
        
    def get_data_by_id(self, collection_name: str, id: str) -> tuple:
        """
        Retrieve data from a specified collection by ID with optional includes.

        Args:
            collection_name (str): The name of the collection to retrieve data from.
            id (str): The unique ID of the document to retrieve.

        Returns:
            Response: A Flask response object containing the retrieved data or an error message.
        """
        filters = request.args.to_dict()
        includes = filters.pop('include', '').split(',')
        try:
            data = db.find_by_key_value(collection_name, {'id': id}, includes)
            if not data:
                return jsonify({"error": "No data found"}), 404
            return jsonify(data), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def delete_data_by_id(self, collection_name: str, id: str) -> tuple:
        """
        Delete data from a specified collection by ID.

        Args:
            collection_name (str): The name of the collection to delete data from.
            id (str): The unique ID of the document to delete.

        Returns:
            Response: A Flask response object containing the count of deleted documents or an error message.
        """
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

    def generate_token(self, collection_name: str, id: str) -> tuple:
        """
        Generate a new token for a given user.

        Args:
            id (str): The unique ID of the user.

        Returns:
            Response: A Flask response object containing the new token or an error message.
        """
        user = db.find_by_key_value(collection_name, {'id': id})
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_token = str(uuid.uuid4())
        if 'tokens' not in user[0]:
            user[0]['tokens'] = []
        user[0]['tokens'].append(new_token)
        db.update_user_tokens(id, user[0]['tokens'])

        return jsonify({"new_token": new_token}), 201

    def upsert_data(self, collection_name: str, id: str = None) -> tuple:
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
