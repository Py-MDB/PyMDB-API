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
routes = Blueprint('user_routes', __name__)


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
