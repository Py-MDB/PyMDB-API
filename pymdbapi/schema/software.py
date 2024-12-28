software_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'slug': {'type': 'string', 'required': True},
    'created': {'type': 'string', 'required': False},
    'description': {'type': 'string', 'required': False},
    'state': {'type': 'string', 'required': True},
    'version': {'type': 'string', 'required': True},
    'type': {'type': 'string', 'required': True},
    'license': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    }
}
