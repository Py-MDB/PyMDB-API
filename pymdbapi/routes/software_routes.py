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
routes = Blueprint('software_routes', __name__)


@routes.route('/operating-systems', methods=['GET'])
@authenticate(required_privilege=1)
def get_operating_systems():
    return routehelper.get_data('operating_systems')

@routes.route('/operating-systems/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_operating_system_by_id(id):
    return routehelper.get_data_by_id('operating_systems', id)

@routes.route('/operating-systems', methods=['POST'])
@authenticate(required_privilege=3)
def create_operating_system():
    return routehelper.upsert_data('operating_systems')

@routes.route('/operating-systems/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_operating_system(id):
    return routehelper.delete_data_by_id('operating_systems', id)

@routes.route('/operating-systems/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_operating_system_by_id(id):
    return routehelper.upsert_data('operating_systems', id)

@routes.route('/licenses', methods=['GET'])
@authenticate(required_privilege=1)
def get_licenses():
    return routehelper.get_data('licenses')

@routes.route('/licenses/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_licenses_by_id(id):
    return routehelper.get_data_by_id('licenses', id)

@routes.route('/licenses', methods=['POST'])
@authenticate(required_privilege=3)
def create_licenses():
    return routehelper.upsert_data('licenses')

@routes.route('/licenses/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_licenses(id):
    return routehelper.delete_data_by_id('licenses', id)

@routes.route('/licenses/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_licenses_by_id(id):
    return routehelper.upsert_data('licenses', id)

@routes.route('/software', methods=['GET'])
@authenticate(required_privilege=1)
def get_software():
    return routehelper.get_data('software')

@routes.route('/software/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_software_by_id(id):
    return routehelper.get_data_by_id('software', id)

@routes.route('/software', methods=['POST'])
@authenticate(required_privilege=3)
def create_software():
    return routehelper.upsert_data('software')

@routes.route('/software/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_software(id):
    return routehelper.delete_data_by_id('software', id)

@routes.route('/software/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_software_by_id(id):
    return routehelper.upsert_data('software', id)
