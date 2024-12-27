"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

class DatabaseSchema:
    def __init__(self):
        self.hardware_schema = {
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
                        'type': 'array',
                        'schema': {
                            'drive_type': {'type': 'string', 'required': True},
                            'capacity': {'type': 'string', 'required': True},
                            'interface': {'type': 'string', 'required': True}
                        }
                    }
                }
            },
            'interfaces': {
                'type': 'array',
                'schema': {
                    'href': {'type': 'string', 'required': False},
                    'id': {'type': 'string', 'required': False},
                }
            }
        }

        self.manufacturers_schema = {
            'id': {'type': 'string', 'required': False},
            'name': {'type': 'string', 'required': True},
            'created': {'type': 'string', 'required': False},
            'slug': {'type': 'string', 'required': True},
        }

        self.facilities_schema = {
            'id': {'type': 'string', 'required': False},
            'name': {'type': 'string', 'required': True},
            'slug': {'type': 'string', 'required': True},
            'location': {'type': 'string', 'required': True},
            'created': {'type': 'string', 'required': False},
            'rack_capacity': {'type': 'integer', 'required': True},
            'state': {'type': 'string', 'required': True},
        }

        self.racks_schema = {
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

        self.licenses_schema = {
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

        self.interfaces_schema = {
            'id': {'type': 'string', 'required': False},
            'name': {'type': 'string', 'required': True},
            'slug': {'type': 'string', 'required': True},
            'created': {'type': 'string', 'required': False},
            'description': {'type': 'string', 'required': False},
            'state': {'type': 'string', 'required': True},
            'type': {'type': 'string', 'required': True},
            'speed': {'type': 'string', 'required': True},
            'duplex': {'type': 'string', 'required': True},
            'mac_address': {'type': 'string', 'required': True},
            'mtu': {'type': 'integer', 'required': True},
            'enabled': {'type': 'boolean', 'required': True},
            'management': {'type': 'boolean', 'required': True},
            'connected': {'type': 'boolean', 'required': True},
            'ipv4_ip': {'type': 'string', 'required': False},
            'ipv6_ip': {'type': 'string', 'required': False},
            'bridged_interfaces': {
                'type': 'array',
                'schema': {
                    'href': {'type': 'string', 'required': False},
                    'id': {'type': 'string', 'required': False},
                }
            },
            'lag_interfaces': {
                'type': 'array',
                'schema': {
                    'href': {'type': 'string', 'required': False},
                    'id': {'type': 'string', 'required': False},
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

        self.software_schema = {
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

        self.operating_systems_schema = {
            'id': {'type': 'string', 'required': False},
            'name': {'type': 'string', 'required': True},
            'created': {'type': 'string', 'required': False},
            'slug': {'type': 'string', 'required': True},
            'version': {'type': 'string', 'required': True},
        }

        self.users_schema = {
            'id': {'type': 'string', 'required': False},
            'username': {'type': 'string', 'required': True},
            'full name': {'type': 'string', 'required': True},
            'created': {'type': 'string', 'required': False},
            'email': {'type': 'string', 'required': False},
            'privilege_level': {'type': 'integer', 'required': True}
        }

        self.app_tokens_schema = {
            'id': {'type': 'string', 'required': False},
            'name': {'type': 'string', 'required': True},
            'created': {'type': 'string', 'required': False},
            'description': {'type': 'string', 'required': False},
            'privilege_level': {'type': 'integer', 'required': True}
        }
