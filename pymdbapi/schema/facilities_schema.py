facilities_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'slug': {'type': 'string', 'required': True},
    'location': {'type': 'string', 'required': True},
    'created': {'type': 'string', 'required': False},
    'region': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'rack_capacity': {'type': 'integer', 'required': True},
    'state': {'type': 'string', 'required': True},
}
