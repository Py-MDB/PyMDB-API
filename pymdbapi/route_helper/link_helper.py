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
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

schema = DatabaseSchema()
db = PyMongoDB()

def get_field_type(collection_name: str, field: str) -> str:
    """
    Determine the type of a field in the schema.

    Args:
        collection_name (str): The name of the collection.
        field (str): The field name to check.

    Returns:
        str: The type of the field ('list', 'dict', or 'unknown').
    """
    collection_schema = getattr(schema, f"{collection_name}_schema")
    if field in collection_schema:
        field_type = collection_schema[field].get('type')
        if field_type == 'list':
            return 'list'
        elif field_type == 'dict':
            return 'dict'
    return 'unknown'

def update_related_field(doc: dict, field: str, related_id: dict, field_type: str):
    """
    Update the related field in the document.

    Args:
        doc (dict): The document to update.
        field (str): The field to update.
        related_id (dict): The related item to add.
        field_type (str): The type of the field ('list' or 'dict').
    """
    if field_type == 'list':
        if field not in doc:
            doc[field] = []
        if related_id not in doc[field]:
            doc[field].append(related_id)
    elif field_type == 'dict':
        if field not in doc:
            doc[field] = {}
        doc[field].update(related_id)

def link_related_items(collection_name: str, id: str, related_field: str, related_collection: str, back_link_field: str) -> tuple:
    """
    Link related items to a document in a specified collection.

    Args:
        collection_name (str): The name of the collection to update.
        id (str): The unique ID of the document to update.
        related_field (str): The field in the document to update with related items.
        related_collection (str): The name of the related collection.
        back_link_field (str): The field in the related document to link back to the main document.

    Returns:
        Response: A Flask response object containing the updated document or an error message.
    """
    addition = request.json
    if isinstance(addition, dict):
        addition = [addition]
    try:
        # Validate the main document exists
        main_doc = db.validate_document_exists(collection_name, id)
        if not main_doc:
            return jsonify({"error": "Main document not found"}), 404

        # Determine the type of the related field
        field_type = get_field_type(collection_name, related_field)

        # Validate and link each related item
        for related_id in addition:
            related_doc = db.validate_document_exists(related_collection, related_id['id'])
            if not related_doc:
                return jsonify({"error": f"Related document with id {related_id['id']} not found"}), 404

            # Update the main document's related field
            update_related_field(main_doc, related_field, related_id, field_type)

            # Update the related document to link back to the main document
            back_link_type = get_field_type(related_collection, back_link_field)
            update_related_field(related_doc, back_link_field, {'id': id}, back_link_type)

            db.update_by_id(related_collection, related_id['id'], related_doc)

        # Update the main document with the new related items
        db.update_by_id(collection_name, id, main_doc)
        return jsonify(main_doc), 200
    except Exception as e:
        logger.error(f"Error linking related items in {collection_name}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

def unlink_related_items(collection_name: str, id: str, related_field: str, related_collection: str, back_link_field: str) -> tuple:
    """
    Unlink related items from a document in a specified collection.

    Args:
        collection_name (str): The name of the collection to update.
        id (str): The unique ID of the document to update.
        related_field (str): The field in the document to update with related items.
        related_collection (str): The name of the related collection.
        back_link_field (str): The field in the related document to unlink from the main document.

    Returns:
        Response: A Flask response object containing the updated document or an error message.
    """
    removal = request.json
    if isinstance(removal, dict):
        removal = [removal]
    try:
        # Validate the main document exists
        main_doc = db.validate_document_exists(collection_name, id)
        if not main_doc:
            return jsonify({"error": "Main document not found"}), 404

        # Validate and unlink each related item
        for related_id in removal:
            related_doc = db.validate_document_exists(related_collection, related_id['id'])
            if not related_doc:
                return jsonify({"error": f"Related document with id {related_id['id']} not found"}), 404

            # Remove the related item from the main document's related field
            if related_field in main_doc:
                if isinstance(main_doc[related_field], list):
                    main_doc[related_field] = [item for item in main_doc[related_field] if item['id'] != related_id['id']]
                elif isinstance(main_doc[related_field], dict):
                    if main_doc[related_field].get('id') == related_id['id']:
                        main_doc[related_field] = {}

            # Update the related document to unlink from the main document
            if back_link_field in related_doc:
                if isinstance(related_doc[back_link_field], list):
                    related_doc[back_link_field] = [item for item in related_doc[back_link_field] if item['id'] != id]
                elif isinstance(related_doc[back_link_field], dict):
                    if related_doc[back_link_field].get('id') == id:
                        related_doc[back_link_field] = {}

            db.update_by_id(related_collection, related_id['id'], related_doc)

        # Update the main document with the removed related items
        db.update_by_id(collection_name, id, main_doc)
        return jsonify(main_doc), 200
    except Exception as e:
        logger.error(f"Error unlinking related items in {collection_name}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
