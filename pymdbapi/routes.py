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

@routes.route('/operating_systems', methods=['GET'])
@authenticate(required_privilege=1)
def get_operating_systems():
    return routehelper.get_data('operating_systems')

@routes.route('/operating_systems/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_operating_system_by_id(id):
    return routehelper.get_data_by_id('operating_systems', id)

@routes.route('/operating_systems', methods=['POST'])
@authenticate(required_privilege=3)
def create_operating_system():
    return routehelper.upsert_data('operating_systems')

@routes.route('/operating_systems/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_operating_system(id):
    return routehelper.delete_data_by_id('operating_systems', id)

@routes.route('/operating_systems/<id>', methods=['PUT'])
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

@routes.route('/app_tokens', methods=['GET'])
@authenticate(required_privilege=3)
def get_app_tokens():
    return routehelper.get_data('app_tokens')

@routes.route('/app_tokens/<id>', methods=['GET'])
@authenticate(required_privilege=3)
def get_app_token_by_id(id):
    return routehelper.get_data_by_id('app_tokens', id)

@routes.route('/app_tokens', methods=['POST'])
@authenticate(required_privilege=5)
def create_app_token():
    return routehelper.upsert_data('app_tokens')

@routes.route('/app_tokens/<id>', methods=['DELETE'])
@authenticate(required_privilege=5)
def delete_app_token(id):
    return routehelper.delete_data_by_id('app_tokens', id)

@routes.route('/app_tokens/<id>/generate_token', methods=['POST'])
@authenticate(required_privilege=5)
def generate_app_token(id):
    return routehelper.generate_token('app_tokens', id)

@routes.route('/app_tokens/<id>', methods=['PUT'])
@authenticate(required_privilege=5)
def upsert_app_token_by_id(id):
    return routehelper.upsert_data('app_tokens', id)
