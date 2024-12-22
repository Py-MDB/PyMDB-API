

class DatabaseSchema:
    def __init__(self):
        self.hardware_schema = {
            'id': {'type': 'string', 'required': True},
            'name': {'type': 'string', 'required': True},
            'type': {'type': 'string', 'required': True},
            'state': {'type': 'string', 'required': True},
            'operating_system': {'type': 'string', 'required': False},
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
