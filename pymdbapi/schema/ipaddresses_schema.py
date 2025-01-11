ipaddresses_schema = {
    'id': {'type': 'string', 'required': False},
    'ip_address': {'type': 'string', 'required': True},
    'subnet': {'type': 'string', 'required': True},
    'state': {'type': 'string', 'required': False},
    'type': {'type': 'string', 'required': False},
    'hardware': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'network': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    },
    'created': {'type': 'string', 'required': False},
    'description': {'type': 'string', 'required': False},
    'dns_name': {'type': 'string', 'required': False},
    'mac_address': {'type': 'string', 'required': False},
    'interface': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    }
}
