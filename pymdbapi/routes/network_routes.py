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


routehelper = RouteHelper()
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