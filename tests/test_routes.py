import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from pymdbapi.routes import routes

class TestRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(routes)
        cls.client = cls.app.test_client()

    @patch('pymdbapi.routes.db')
    def test_home(self, mock_db):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Welcome to the PyMDB API!"})

    @patch('pymdbapi.routes.db')
    def test_create_data(self, mock_db):
        sample_hardware = {
            'id': 'mock_id',
            'name': 'test1',
            'type': 'server',
            'specs': {
                'cpu': 'Intel Xeon',
                'ram': '128GB',
                'storage': '512GB SSD'
            },
            'operating_system': 'debian',
            'state': 'active',
        }
        mock_db.insert.return_value = 'mock_id'
        response = self.client.post('/hardware', json=sample_hardware)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'inserted_id': 'mock_id'})

    @patch('pymdbapi.routes.db')
    def test_get_data(self, mock_db):
        mock_db.get_all.return_value = [{'name': 'test1'}]
        response = self.client.get('/hardware')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    @patch('pymdbapi.routes.db')
    def test_get_data_by_key_value(self, mock_db):
        mock_db.find_by_key_value.return_value = [{'name': 'test1'}]
        response = self.client.get('/hardware', query_string={'name': 'test1'})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)
        self.assertGreater(len(response.json), 0)

    @patch('pymdbapi.routes.db')
    def test_delete_data(self, mock_db):
        mock_db.delete_by_id.return_value = 1
        response = self.client.delete('/hardware', query_string={'id': 'mock_id'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'deleted_count': 1})

if __name__ == '__main__':
    unittest.main()
