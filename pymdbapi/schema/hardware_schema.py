hardware_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'type': {'type': 'string', 'required': True},
    'model': {'type': 'string', 'required': False},
    'created': {'type': 'string', 'required': False},
    'state': {'type': 'string', 'required': True},
    'operating_system': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'manufacturer': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'facility': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
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
    'rack': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'specs': {
        'type': 'dict',
        'schema': {
            'cpu': {'type': 'string', 'required': True},
            'ram': {'type': 'string', 'required': True},
            'storage': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        'drive_type': {'type': 'string', 'required': True},
                        'capacity': {'type': 'string', 'required': True},
                        'interface': {'type': 'string', 'required': True},
                        'serial': {'type': 'string', 'required': False},
                        'manufacturer': {'type': 'string', 'required': False},
                        'product_id' : {'type': 'string', 'required': False},
                    }
                }
            }
        }
    },
    'interfaces': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'href': {'type': 'string', 'required': False},
                'id': {'type': 'string', 'required': False},
            }
        }
    }
}
