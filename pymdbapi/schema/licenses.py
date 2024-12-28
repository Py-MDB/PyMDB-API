licenses_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'slug': {'type': 'string', 'required': True},
    'created': {'type': 'string', 'required': False},
    'description': {'type': 'string', 'required': False},
    'product_key': {'type': 'string', 'required': True},
    'expiration': {'type': 'string', 'required': False},
    'state': {'type': 'string', 'required': True},
    'software': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'size': {'type': 'integer', 'required': False}
}
