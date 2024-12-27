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
routes = Blueprint('routes', __name__)


@routes.route('/')
@authenticate()
def home():
    return jsonify({"message": "Welcome to the PyMDB API!"})

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

@routes.route('/facilities', methods=['GET'])
@authenticate(required_privilege=1)
def get_facilities():
    return routehelper.get_data('facilities')

@routes.route('/facilities/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_facility_by_id(id):
    return routehelper.get_data_by_id('facilities', id)

@routes.route('/facilities', methods=['POST'])
@authenticate(required_privilege=3)
def create_facility():
    return routehelper.upsert_data('facilities')

@routes.route('/facilities/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_facility(id):
    return routehelper.delete_data_by_id('facilities', id)

@routes.route('/facilities/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_facility_by_id(id):
    return routehelper.upsert_data('facilities', id)

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

@routes.route('/users', methods=['GET'])
@authenticate(required_privilege=4)
def get_users():
    return routehelper.get_data('users')

@routes.route('/users/<id>', methods=['GET'])
@authenticate(required_privilege=4)
def get_user_by_id(id):
    return routehelper.get_data_by_id('users', id)

@routes.route('/users', methods=['POST'])
@authenticate(required_privilege=5)
def create_user():
    return routehelper.upsert_data('users')

@routes.route('/users/<id>', methods=['DELETE'])
@authenticate(required_privilege=5)
def delete_user(id):
    return routehelper.delete_data_by_id('users', id)

@routes.route('/users/<id>/generate-token', methods=['POST'])
@authenticate(required_privilege=5)
def generate_user_token(id):
    return routehelper.generate_token('users', id)

@routes.route('/users/<id>', methods=['PUT'])
@authenticate(required_privilege=5)
def upsert_user_by_id(id):
    return routehelper.upsert_data('users', id)

@routes.route('/app-tokens', methods=['GET'])
@authenticate(required_privilege=3)
def get_app_tokens():
    return routehelper.get_data('app_tokens')

@routes.route('/app-tokens/<id>', methods=['GET'])
@authenticate(required_privilege=3)
def get_app_token_by_id(id):
    return routehelper.get_data_by_id('app_tokens', id)

@routes.route('/app-tokens', methods=['POST'])
@authenticate(required_privilege=5)
def create_app_token():
    return routehelper.upsert_data('app_tokens')

@routes.route('/app-tokens/<id>', methods=['DELETE'])
@authenticate(required_privilege=5)
def delete_app_token(id):
    return routehelper.delete_data_by_id('app_tokens', id)

@routes.route('/app-tokens/<id>/generate-token', methods=['POST'])
@authenticate(required_privilege=5)
def generate_app_token(id):
    return routehelper.generate_token('app_tokens', id)

@routes.route('/app-tokens/<id>', methods=['PUT'])
@authenticate(required_privilege=5)
def upsert_app_token_by_id(id):
    return routehelper.upsert_data('app_tokens', id)

@routes.route('/manufacturers', methods=['GET'])
@authenticate(required_privilege=1)
def get_manufacturers():
    return routehelper.get_data('manufacturers')

@routes.route('/manufacturers/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_manufacturers_by_id(id):
    return routehelper.get_data_by_id('manufacturers', id)

@routes.route('/manufacturers', methods=['POST'])
@authenticate(required_privilege=3)
def create_manufacturers():
    return routehelper.upsert_data('manufacturers')

@routes.route('/manufacturers/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_manufacturers(id):
    return routehelper.delete_data_by_id('manufacturers', id)

@routes.route('/manufacturers/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_manufacturers_by_id(id):
    return routehelper.upsert_data('manufacturers', id)

@routes.route('/racks', methods=['GET'])
@authenticate(required_privilege=1)
def get_racks():
    return routehelper.get_data('racks')

@routes.route('/racks/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_racks_by_id(id):
    return routehelper.get_data_by_id('racks', id)

@routes.route('/racks', methods=['POST'])
@authenticate(required_privilege=3)
def create_racks():
    return routehelper.upsert_data('racks')

@routes.route('/racks/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_racks(id):
    return routehelper.delete_data_by_id('racks', id)

@routes.route('/racks/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_racks_by_id(id):
    return routehelper.upsert_data('racks', id)

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
