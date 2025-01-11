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
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = PyMongoDB()

def get_data(collection_name: str, filters: dict = None) -> tuple:
    """
    Retrieve data from a specified collection with optional filters and includes.

    Args:
        collection_name (str): The name of the collection to retrieve data from.
        filters (dict, optional): A dictionary of filters to apply to the query.

    Returns:
        Response: A Flask response object containing the retrieved data or an error message.
    """
    if filters is None:
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
    
def get_data_by_id(collection_name: str, id: str) -> tuple:
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
