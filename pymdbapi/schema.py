

class DatabaseSchema:
    def __init__(self):
        self.hardware_schema = {
            'id': {'type': 'string', 'required': True},
            'name': {'type': 'string', 'required': True},
            'type': {'type': 'string', 'required': True},
            'specs': {
                'type': 'dict',
                'schema': {
                    'cpu': {'type': 'string', 'required': True},
                    'ram': {'type': 'string', 'required': True},
                    'storage': {'type': 'string', 'required': True}
                }
            }
        }
