import unittest
import logging
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify


class TestRoutes(unittest.TestCase):
    def setUp(self):
        logging.getLogger('pymongo').setLevel(logging.WARNING)
        self.app = Flask(__name__)
        with patch('pymdbapi.auth.authenticate', new=self.mock_authenticate):
            from pymdbapi.routes import routes
            self.app.register_blueprint(routes)
        self.client = self.app.test_client()

    def mock_authenticate(self, *args, **kwargs):
        def decorator(f):
            return f
        return decorator

    @patch('pymdbapi.route_helper.RouteHelper.get_data')
    def test_get_hardware(self, mock_get_data):
        mock_get_data.return_value = MagicMock(status_code=200)
        mock_get_data.return_value.get_json.return_value = {"hardware": []}
        response = self.client.get('/hardware')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"hardware": []})

    @patch('pymdbapi.route_helper.RouteHelper.get_data_by_id')
    def test_get_hardware_by_id(self, mock_get_data_by_id):
        mock_get_data_by_id.return_value = MagicMock(status_code=200)
        mock_get_data_by_id.return_value.get_json.return_value = {"id": "123"}
        response = self.client.get('/hardware/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"id": "123"})

    @patch('pymdbapi.route_helper.RouteHelper.add_data')
    def test_create_hardware(self, mock_add_data):
        mock_add_data.return_value = MagicMock(status_code=201)
        mock_add_data.return_value.get_json.return_value = {"inserted_id": "123"}
        response = self.client.post('/hardware', json={"name": "New Hardware"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"inserted_id": "123"})

    @patch('pymdbapi.route_helper.RouteHelper.delete_data_by_id')
    def test_delete_hardware(self, mock_delete_data_by_id):
        mock_delete_data_by_id.return_value = MagicMock(status_code=200)
        mock_delete_data_by_id.return_value.get_json.return_value = {"deleted_count": 1}
        response = self.client.delete('/hardware/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"deleted_count": 1})

    @patch('pymdbapi.route_helper.RouteHelper.upsert_data')
    def test_upsert_hardware_by_id(self, mock_upsert_data):
        mock_upsert_data.return_value = MagicMock(status_code=200)
        mock_upsert_data.return_value.get_json.return_value = {"updated_id": "123"}
        response = self.client.put('/hardware/123', json={"name": "Updated Hardware"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"updated_id": "123"})

    @patch('pymdbapi.route_helper.RouteHelper.upsert_data')
    def test_create_hardware_with_upsert(self, mock_upsert_data):
        mock_upsert_data.return_value = MagicMock(status_code=201)
        mock_upsert_data.return_value.get_json.return_value = {"inserted_id": "123"}
        response = self.client.post('/hardware', json={"name": "New Hardware"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"inserted_id": "123"})

if __name__ == '__main__':
    unittest.main()
