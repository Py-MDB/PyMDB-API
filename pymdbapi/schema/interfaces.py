interfaces_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'slug': {'type': 'string', 'required': True},
    'created': {'type': 'string', 'required': False},
    'description': {'type': 'string', 'required': False},
    'state': {'type': 'string', 'required': True},
    'type': {'type': 'string', 'required': True},
    'speed': {'type': 'string', 'required': False},
    'duplex': {'type': 'string', 'required': False},
    'mac_address': {'type': 'string', 'required': True},
    'mtu': {'type': 'integer', 'required': False},
    'enabled': {'type': 'boolean', 'required': True},
    'management': {'type': 'boolean', 'required': True},
    'connected': {'type': 'boolean', 'required': True},
    'ipv4_ip': {'type': 'string', 'required': False},
    'ipv6_ip': {'type': 'string', 'required': False},
    'bridged_interfaces': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'href': {'type': 'string', 'required': False},
                'id': {'type': 'string', 'required': False},
            }
        }
    },
    'lag_interfaces': {
        'type': 'list',
        'schema': {
            'type': 'dict',
            'schema': {
                'href': {'type': 'string', 'required': False},
                'id': {'type': 'string', 'required': False},
            }
        }
    },
    'hardware': {
        'type': 'dict',
        'schema': {
            'href': {'type': 'string', 'required': False},
            'id': {'type': 'string', 'required': False},
        }
    }
}
