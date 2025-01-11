"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import Blueprint, jsonify
from pymdbapi.route_helper import RouteHelper
from pymdbapi.auth import authenticate
from pymdbapi.ipam.ipam import Ipam


routehelper = RouteHelper()
ipam = Ipam()
routes = Blueprint('network_routes', __name__)

@routes.route('/interfaces', methods=['GET'])
@authenticate(required_privilege=1)
def get_interfaces():
    return routehelper.get_data('interfaces')

@routes.route('/interfaces/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_interfaces_by_id(id):
    return routehelper.get_data_by_id('interfaces', id)

@routes.route('/interfaces', methods=['POST'])
@authenticate(required_privilege=3)
def create_interfaces():
    return routehelper.upsert_data('interfaces')

@routes.route('/interfaces/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_interfaces(id):
    return routehelper.delete_data_by_id('interfaces', id)

@routes.route('/interfaces/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_interfaces_by_id(id):
    return routehelper.upsert_data('interfaces', id)

@routes.route('/interfaces/<id>/connect-interface', methods=['POST'])
@authenticate(required_privilege=3)
def connect_interface(id):
    return routehelper.link_related_items('interfaces', id, 'connected_interface', 'interfaces', 'connected_interface')

@routes.route('/networks', methods=['GET'])
@authenticate(required_privilege=1)
def get_networks():
    return routehelper.get_data('networks')

@routes.route('/networks/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_networks_by_id(id):
    return routehelper.get_data_by_id('networks', id)

@routes.route('/networks', methods=['POST'])
@authenticate(required_privilege=3)
def create_networks():
    return ipam.add_network()

@routes.route('/networks/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_networks(id):
    return routehelper.delete_data_by_id('networks', id)

@routes.route('/networks/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_networks_by_id(id):
    return routehelper.upsert_data('networks', id)

@routes.route('/ipaddresses', methods=['GET'])
@authenticate(required_privilege=1)
def get_ipaddresses():
    return routehelper.get_data('ipaddresses')

@routes.route('/ipaddresses/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_ipaddresses_by_id(id):
    return routehelper.get_data_by_id('ipaddresses', id)

@routes.route('/ipaddresses', methods=['POST'])
@authenticate(required_privilege=3)
def create_ipaddresses():
    return routehelper.upsert_data('ipaddresses')

@routes.route('/ipaddresses/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_ipaddresses(id):
    return routehelper.delete_data_by_id('ipaddresses', id)

@routes.route('/ipaddresses/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_ipaddresses_by_id(id):
    return routehelper.upsert_data('ipaddresses', id)
