import unittest
from unittest.mock import patch, MagicMock
from pymdbapi.mongodb import PyMongoDB

class TestPyMongoDB(unittest.TestCase):
    @patch('pymdbapi.mongodb.MongoClient')
    def setUp(self, MockMongoClient):
        self.mock_client = MockMongoClient.return_value
        self.mock_db = self.mock_client.__getitem__.return_value
        self.mongodb = PyMongoDB()

    def test_get_all(self):
        mock_collection = self.mock_db.__getitem__.return_value
        mock_collection.find.return_value = [{'_id': '123', 'name': 'test'}]
        
        result = self.mongodb.get_all('test_collection')
        
        self.assertEqual(result, [{'name': 'test'}])
        mock_collection.find.assert_called_once()

    def test_insert(self):
        mock_collection = self.mock_db.__getitem__.return_value
        mock_collection.find_one.return_value = None
        mock_collection.insert_one.return_value = MagicMock(inserted_id='123')
        
        data = {'name': 'test'}
        result = self.mongodb.insert('test_collection', data)
        
        self.assertIsNotNone(result)
        self.assertIn('id', data)
        mock_collection.insert_one.assert_called_once_with(data)

    def test_find_by_key_value(self):
        mock_collection = self.mock_db.__getitem__.return_value
        mock_collection.find.return_value = [{'_id': '123', 'name': 'test'}]
        
        result = self.mongodb.find_by_key_value('test_collection', {'name': 'test'})
        
        self.assertEqual(result, [{'name': 'test'}])
        mock_collection.find.assert_called_once_with({'name': 'test'})

    def test_delete_by_id(self):
        mock_collection = self.mock_db.__getitem__.return_value
        mock_collection.delete_one.return_value = MagicMock(deleted_count=1)
        
        result = self.mongodb.delete_by_id('test_collection', '123')
        
        self.assertEqual(result, 1)
        mock_collection.delete_one.assert_called_once_with({'id': '123'})

if __name__ == '__main__':
    unittest.main()
