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

    def get_all(self, collection_name):
        collection = self.db[collection_name]
        data = list(collection.find())
        for item in data:
            item.pop('_id', None)
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

    def find_by_key_value(self, collection_name, filters):
        collection = self.db[collection_name]
        data = list(collection.find(filters))
        for item in data:
            item.pop('_id', None)
        return data

    def delete_by_id(self, collection_name, id):
        collection = self.db[collection_name]
        result = collection.delete_one({"id": id})
        return result.deleted_count
