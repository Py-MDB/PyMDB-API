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


db = PyMongoDB()
schema = DatabaseSchema()


class RouteHelper:
    def __init__(self):
        pass

    def get_data(self, collection_name: str):
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
        
    def get_data_by_id(self, collection_name: str, id: str):
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
        
    def add_data(self, collection_name: str):
        """
        Add new data to a specified collection.

        Args:
            collection_name (str): The name of the collection to add data to.

        Returns:
            Response: A Flask response object containing the inserted ID or an error message.
        """
        collection_schema = getattr(schema, f"{collection_name}_schema")
        validator = Validator(collection_schema)
        data = request.json
        if not validator.validate(data):
            return jsonify({"error": "Invalid data", "details": validator.errors}), 400
        inserted_id = db.insert(collection_name, data)
        return jsonify({"inserted_id": inserted_id}), 201
    
    def delete_data_by_id(self, collection_name: str, id: str):
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
