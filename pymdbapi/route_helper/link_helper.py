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
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = PyMongoDB()

def link_related_items(collection_name: str, id: str, related_field: str, related_collection: str) -> tuple:
    """
    Link related items to a document in a specified collection.

    Args:
        collection_name (str): The name of the collection to update.
        id (str): The unique ID of the document to update.
        related_field (str): The field in the document to update with related items.
        related_collection (str): The name of the related collection.

    Returns:
        Response: A Flask response object containing the updated document or an error message.
    """
    addition = request.json
    if isinstance(addition, list):
        addition = addition
    elif isinstance(addition, dict):
        addition = [addition]
    try:
        # Validate the main document exists
        main_doc = db.find_by_key_value(collection_name, {'id': id})
        if not main_doc:
            return jsonify({"error": "Main document not found"}), 404

        # Validate and link each related item
        for related_id in addition:
            related_doc = db.find_by_key_value(related_collection, {'id': related_id['id']})
            if not related_doc:
                return jsonify({"error": f"Related document with id {related_id['id']} not found"}), 404

            # Add the related item to the main document's related field
            if related_field not in main_doc[0]:
                main_doc[0][related_field] = [] if isinstance(related_id, dict) else {}
            if isinstance(main_doc[0][related_field], list):
                if related_id not in main_doc[0][related_field]:
                    main_doc[0][related_field].append(related_id)
            elif isinstance(main_doc[0][related_field], dict):
                main_doc[0][related_field].update(related_id)

            # Update the related document to link back to the main document
            if 'hardware' not in related_doc[0]:
                related_doc[0]['hardware'] = {'id': id}
            else:
                if isinstance(related_doc[0]['hardware'], list):
                    if {'id': id} not in related_doc[0]['hardware']:
                        related_doc[0]['hardware'].append({'id': id})
                elif isinstance(related_doc[0]['hardware'], dict):
                    related_doc[0]['hardware']['id'] = id
            db.update_by_id(related_collection, related_id['id'], related_doc[0])

        # Update the main document with the new related items
        db.update_by_id(collection_name, id, main_doc[0])
        return jsonify(main_doc[0]), 200
    except Exception as e:
        logger.error(f"Error linking related items in {collection_name}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

def unlink_related_items(collection_name: str, id: str, related_field: str, related_collection: str) -> tuple:
    """
    Unlink related items from a document in a specified collection.

    Args:
        collection_name (str): The name of the collection to update.
        id (str): The unique ID of the document to update.
        related_field (str): The field in the document to update with related items.
        related_collection (str): The name of the related collection.

    Returns:
        Response: A Flask response object containing the updated document or an error message.
    """
    removal = request.json
    if isinstance(removal, list):
        removal = removal
    elif isinstance(removal, dict):
        removal = [removal]
    try:
        # Validate the main document exists
        main_doc = db.find_by_key_value(collection_name, {'id': id})
        if not main_doc:
            return jsonify({"error": "Main document not found"}), 404

        # Validate and unlink each related item
        for related_id in removal:
            related_doc = db.find_by_key_value(related_collection, {'id': related_id['id']})
            if not related_doc:
                return jsonify({"error": f"Related document with id {related_id['id']} not found"}), 404

            # Remove the related item from the main document's related field
            if related_field in main_doc[0]:
                if isinstance(main_doc[0][related_field], list):
                    main_doc[0][related_field] = [item for item in main_doc[0][related_field] if item['id'] != related_id['id']]
                elif isinstance(main_doc[0][related_field], dict):
                    if main_doc[0][related_field].get('id') == related_id['id']:
                        main_doc[0][related_field] = {}

            # Update the related document to unlink from the main document
            if 'hardware' in related_doc[0]:
                if isinstance(related_doc[0]['hardware'], list):
                    related_doc[0]['hardware'] = [item for item in related_doc[0]['hardware'] if item['id'] != id]
                elif isinstance(related_doc[0]['hardware'], dict):
                    if related_doc[0]['hardware'].get('id') == id:
                        related_doc[0]['hardware'] = {}

            db.update_by_id(related_collection, related_id['id'], related_doc[0])

        # Update the main document with the removed related items
        db.update_by_id(collection_name, id, main_doc[0])
        return jsonify(main_doc[0]), 200
    except Exception as e:
        logger.error(f"Error unlinking related items in {collection_name}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
