"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import Blueprint
from pymdbapi.route_helper import RouteHelper
from pymdbapi.auth import authenticate


routehelper = RouteHelper()
routes = Blueprint('hardware_routes', __name__)


@routes.route('/hardware', methods=['GET'])
@authenticate(required_privilege=1)
def get_hardware():
    return routehelper.get_data('hardware')

@routes.route('/hardware/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_hardware_by_id(id):
    return routehelper.get_data_by_id('hardware', id)

@routes.route('/hardware', methods=['POST'])
@authenticate(required_privilege=3)
def create_hardware():
    return routehelper.upsert_data('hardware')

@routes.route('/hardware/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_hardware(id):
    return routehelper.delete_data_by_id('hardware', id)

@routes.route('/hardware/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_hardware_by_id(id):
    return routehelper.upsert_data('hardware', id)

@routes.route('/hardware/<id>/link-interfaces', methods=['POST'])
@authenticate(required_privilege=3)
def link_interfaces_to_hardware(id):
    return routehelper.link_related_items('hardware', id, 'interfaces', 'interfaces')

@routes.route('/hardware/<id>/unlink-interfaces', methods=['POST'])
@authenticate(required_privilege=3)
def unlink_interfaces_from_hardware(id):
    return routehelper.unlink_related_items('hardware', id, 'interfaces', 'interfaces')

