import os
from pymongo import MongoClient
from bson import ObjectId
import uuid

class PyMongoDB:
    def __init__(self):
        mongo_user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
        mongo_password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
        mongo_host = os.getenv("MONGO_HOST", "mongodb")
        mongo_port = os.getenv("MONGO_PORT", 27017)
        self.client = MongoClient(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")
        self.db = self.client["pyapi-db"]

    def get_all(self, collection_name, includes=[]):
        collection = self.db[collection_name]
        data = list(collection.find())
        for item in data:
            item.pop('_id', None)
            self._add_includes(item, includes)
            self._add_hrefs(item)
        return data

    def insert(self, collection_name, data):
        collection = self.db[collection_name]
        while True:
            new_uuid = str(uuid.uuid4())
            if not collection.find_one({"id": new_uuid}):
                data['id'] = new_uuid
                break
        result = collection.insert_one(data)
        return data['id']

    def find_by_key_value(self, collection_name, filters, includes=[]):
        collection = self.db[collection_name]
        data = list(collection.find(filters))
        for item in data:
            item.pop('_id', None)
            self._add_includes(item, includes)
            self._add_hrefs
        return data

    def delete_by_id(self, collection_name, id):
        collection = self.db[collection_name]
        result = collection.delete_one({"id": id})
        return result.deleted_count

    def _add_includes(self, item, includes):
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

    def _add_hrefs(self, item):
        if 'facility' in item and 'id' in item['facility']:
            item['facility']['href'] = f"/facilities/{item['facility']['id']}"
        if 'operating_system' in item and 'id' in item['operating_system']:
            item['operating_system']['href'] = f"/operating_systems/{item['operating_system']['id']}"
