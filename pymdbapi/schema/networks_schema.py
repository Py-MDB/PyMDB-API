networks_schema = {
    'id': {'type': 'string', 'required': False},
    'name': {'type': 'string', 'required': True},
    'network_address': {'type': 'string', 'required': True},
    'cidr_mask': {'type': 'string', 'required': True},
    'gateway': {'type': 'string', 'required': False},
    'dns_servers': {
        'type': 'list',
        'schema': {
            'type': 'string',
            'required': False
        }
    },
    'dhcp_range': {
        'type': 'dict',
        'schema': {
            'start': {'type': 'string', 'required': False},
            'end': {'type': 'string', 'required': False}
        }
    },
    'created': {'type': 'string', 'required': False},
    'description': {'type': 'string', 'required': False},
    'state': {'type': 'string', 'required': False},
}
