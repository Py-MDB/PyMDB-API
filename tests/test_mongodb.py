import unittest
import logging
from unittest.mock import patch, MagicMock
from pymdbapi.mongodb import PyMongoDB

class TestPyMongoDB(unittest.TestCase):
    @patch('pymdbapi.mongodb.MongoClient')
    def setUp(self, mock_mongo_client):
        logging.getLogger('pymongo').setLevel(logging.WARNING)
        self.mock_client = MagicMock()
        mock_mongo_client.return_value = self.mock_client
        self.db = PyMongoDB()

    @patch('pymdbapi.mongodb.MongoClient')
    def test_get_all(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_collection.find.return_value = [{"id": "123"}]
        self.mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection
        data = self.db.get_all('hardware')
        self.assertEqual(data, [{"id": "123"}])

    @patch('pymdbapi.mongodb.MongoClient')
    @patch('uuid.uuid4', return_value="123")
    def test_insert(self, mock_uuid, mock_mongo_client):
        mock_collection = MagicMock()
        mock_collection.find_one.return_value = None
        mock_collection.insert_one.return_value = MagicMock(inserted_id="123")
        self.mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection
        inserted_id = self.db.insert('hardware', {"name": "New Hardware"})
        self.assertEqual(inserted_id, "123")

    @patch('pymdbapi.mongodb.MongoClient')
    def test_find_by_key_value(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_collection.find.return_value = [{"id": "123"}]
        self.mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection
        data = self.db.find_by_key_value('hardware', {"id": "123"})
        self.assertEqual(data, [{"id": "123"}])

    @patch('pymdbapi.mongodb.MongoClient')
    def test_delete_by_id(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_collection.delete_one.return_value = MagicMock(deleted_count=1)
        self.mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection
        deleted_count = self.db.delete_by_id('hardware', "123")
        self.assertEqual(deleted_count, 1)

    @patch('pymdbapi.mongodb.MongoClient')
    def test_update_by_id(self, mock_mongo_client):
        mock_collection = MagicMock()
        mock_collection.update_one.return_value = MagicMock(modified_count=1)
        self.mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection
        updated_count = self.db.update_by_id('hardware', "123", {"name": "Updated Hardware"})
        self.assertEqual(updated_count, 1)

if __name__ == '__main__':
    unittest.main()
