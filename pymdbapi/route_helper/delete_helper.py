"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import jsonify
from pymdbapi.mongodb import PyMongoDB
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = PyMongoDB()

def delete_data_by_id(collection_name: str, id: str) -> tuple:
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
