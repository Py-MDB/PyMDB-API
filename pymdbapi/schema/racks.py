racks_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'slug': {'type': 'string', 'required': True},
    'cage': {'type': 'string', 'required': False},
    'created': {'type': 'string', 'required': False},
    'u_space': {'type': 'integer', 'required': True},
    'facility': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
}
