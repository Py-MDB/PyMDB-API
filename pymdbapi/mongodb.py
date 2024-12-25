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
        print(f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/")

    def get_all(self, collection_name, includes=[]):
        collection = self.db[collection_name]
        data = list(collection.find())
        for item in data:
            item.pop('_id', None)
            print(f"item: {item}")
            print(f"includes: {includes}")
            self._add_includes(item, includes)
            if 'facility' in item and 'id' in item['facility']:
                item['facility']['href'] = f"/facilities/{item['facility']['id']}"
            if 'operating_system' in item and 'id' in item['operating_system']:
                item['operating_system']['href'] = f"/operating_systems/{item['operating_system']['id']}"
        return data

    def insert(self, collection_name, data):
        collection = self.db[collection_name]
        while True:
            new_uuid = str(uuid.uuid4())
            if not collection.find_one({"id": new_uuid}):
                data['id'] = new_uuid
                break
        result = collection.insert_one(data)
        return result

    def find_by_key_value(self, collection_name, filters, includes=[]):
        collection = self.db[collection_name]
        data = list(collection.find(filters))
        for item in data:
            item.pop('_id', None)
            self._add_includes(item, includes)
            if 'facility' in item and 'id' in item['facility']:
                item['facility']['href'] = f"/facilities/{item['facility']['id']}"
            if 'operating_system' in item and 'id' in item['operating_system']:
                item['operating_system']['href'] = f"/operating_systems/{item['operating_system']['id']}"
        return data

    def delete_by_id(self, collection_name, id):
        collection = self.db[collection_name]
        result = collection.delete_one({"id": id})
        return result.deleted_count

    def _add_includes(self, item, includes):
        for include in includes:
            if include == 'facilities':
                singular_include = 'facility'
            else:
                singular_include = include.rstrip('s')
                
            if singular_include in item and 'id' in item[singular_include]:
                print(f"include: {include}", flush=True)
                full_item = self.db[include].find_one({"id": item[singular_include]['id']})
                print(full_item, flush=True)
                if full_item:
                    full_item.pop('_id', None)
                    item[singular_include] = full_item
