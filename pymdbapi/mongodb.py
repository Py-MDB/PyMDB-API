"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

import os
from pymongo import MongoClient
from bson import ObjectId
import datetime
import uuid

class PyMongoDB:
    def __init__(self):
        """
        Initialize the MongoDB client and connect to the database.
        """
        mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
        mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        mongo_host = os.getenv("MONGO_HOST", "mongodb")
        mongo_port = os.getenv("MONGO_PORT", 27017)
        self.client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
        self.db = self.client["pyapi-db"]

    def get_all(self, collection_name: str, includes: list=[]) -> dict:
        """
        Retrieve all documents from a specified collection with optional includes.

        Args:
            collection_name (str): The name of the collection to retrieve data from.
            includes (list): A list of related documents to include in the response.

        Returns:
            dict: A list of documents from the collection.
        """
        collection = self.db[collection_name]
        data = list(collection.find())
        for item in data:
            item.pop('_id', None)
            self._add_includes(item, includes)
            self._add_hrefs(item)
        return data

    def insert(self, collection_name: str, data: dict) -> str:
        """
        Insert a new document into a specified collection and return the inserted ID.

        Args:
            collection_name (str): The name of the collection to insert data into.
            data (dict): The data to insert into the collection.

        Returns:
            str: The ID of the inserted document.
        """
        collection = self.db[collection_name]
        while True:
            new_uuid = str(uuid.uuid4())
            data['created'] = datetime.datetime.now().isoformat()
            if not collection.find_one({"id": new_uuid}):
                data['id'] = new_uuid
                break
        result = collection.insert_one(data)
        return data['id']

    def find_by_key_value(self, collection_name: str, filters: dict, includes: list=[]) -> dict:
        """
        Find documents in a specified collection by key-value filters with optional includes.

        Args:
            collection_name (str): The name of the collection to retrieve data from.
            filters (dict): The key-value filters to apply to the query.
            includes (list): A list of related documents to include in the response.

        Returns:
            dict: A list of documents that match the filters.
        """
        collection = self.db[collection_name]
        data = list(collection.find(filters))
        for item in data:
            item.pop('_id', None)
            self._add_includes(item, includes)
            self._add_hrefs(item)
        return data

    def delete_by_id(self, collection_name: str, id: str) -> int:
        """
        Delete a document from a specified collection by ID and return the count of deleted documents.

        Args:
            collection_name (str): The name of the collection to delete data from.
            id (str): The unique ID of the document to delete.

        Returns:
            int: The count of deleted documents.
        """
        collection = self.db[collection_name]
        result = collection.delete_one({"id": id})
        return result.deleted_count

    def update_user_tokens(self, user_id: str, tokens: list) -> None:
        """
        Update the tokens for a given user.

        Args:
            user_id (str): The unique ID of the user.
            tokens (list): The list of tokens to update for the user.
        """
        collection = self.db['users']
        collection.update_one({'id': user_id}, {'$set': {'tokens': tokens}})

    def update_by_id(self, collection_name: str, id: str, data: dict) -> int:
        """
        Update a document in a specified collection by ID.

        Args:
            collection_name (str): The name of the collection to update data in.
            id (str): The unique ID of the document to update.
            data (dict): The data to update in the document.

        Returns:
            int: The count of updated documents.
        """
        collection = self.db[collection_name]
        result = collection.update_one({"id": id}, {"$set": data})
        return result.modified_count

    def _add_includes(self, item: dict, includes: list) -> None:
        """
        Add included related documents to the item.

        Args:
            item (dict): The document to add includes to.
            includes (list): A list of related documents to include in the item.
        """
        include_transmute = {
            'facility': 'facilities'
        }
        for include in includes:
            if include in item and 'id' in item[include]:
                if include in include_transmute:
                    collection_name = include_transmute[include]
                else:
                    collection_name = include + 's'
                full_item = self.db[collection_name].find_one({"id": item[include]['id']})
                if full_item:
                    full_item.pop('_id', None)
                    item[include] = full_item

    def _add_hrefs(self, item: dict) -> None:
        """
        Create href links from the uuids within linked documents.

        Args:
            item (dict): The document to add href links to.
        """
        href_transmute = [
            'facility',
            'operating_system',
            'hardware',
            'bridged_interfaces',
            'lag_interfaces',
            'license',
            'manufacturer',
            'rack',
            'interfaces',
            'software',
        ]
        for key in href_transmute:
            if key in item and 'id' in item[key]:
                item[key]['href'] = f"/{key.replace('_', '-')}s/{item[key]['id']}"

