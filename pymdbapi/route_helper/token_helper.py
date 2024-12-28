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
import uuid
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = PyMongoDB()

def generate_token(collection_name: str, id: str) -> tuple:
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
