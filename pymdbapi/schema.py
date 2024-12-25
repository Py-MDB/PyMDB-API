

class DatabaseSchema:
    def __init__(self):
        self.hardware_data_schema = {
            'id': {'type': 'string', 'required': False},
            'name': {'type': 'string', 'required': True},
            'type': {'type': 'string', 'required': True},
            'state': {'type': 'string', 'required': True},
            'operating_system': {
                'type': 'dict',
                'schema': {
                    'href': {'type': 'string', 'required': False},
                    'id': {'type': 'string', 'required': False},
                    'name': {'type': 'string', 'required': False},
                    'slug': {'type': 'string', 'required': False},
                    'version': {'type': 'string', 'required': False}
                }
            },
            'facility': {
                'type': 'dict',
                'schema': {
                    'href': {'type': 'string', 'required': False},
                    'id': {'type': 'string', 'required': False},
                    'name': {'type': 'string', 'required': False},
                    'slug': {'type': 'string', 'required': False},
                    'location': {'type': 'string', 'required': False},
                    'capacity': {'type': 'integer', 'required': False},
                    'state': {'type': 'string', 'required': False}
                }
            },
            'management': {
                'type': 'dict',
                'schema': {
                    'ip': {'type': 'string', 'required': False},
                    'username': {'type': 'string', 'required': False},
                    'password': {'type': 'string', 'required': False}
                }
            },
            'specs': {
                'type': 'dict',
                'schema': {
                    'cpu': {'type': 'string', 'required': True},
                    'ram': {'type': 'string', 'required': True},
                    'storage': {'type': 'string', 'required': True}
                }
            }
        }
        self.facilities_schema = {
            'id': {'type': 'string', 'required': True},
            'name': {'type': 'string', 'required': True},
            'slug': {'type': 'string', 'required': True},
            'location': {'type': 'string', 'required': True},
            'capacity': {'type': 'integer', 'required': True},
            'state': {'type': 'string', 'required': True},
        }
        self.operating_systems_schema = {
            'id': {'type': 'string', 'required': True},
            'name': {'type': 'string', 'required': True},
            'slug': {'type': 'string', 'required': True},
            'version': {'type': 'string', 'required': True},
        }
