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


routehelper = RouteHelper()
routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    return jsonify({"message": "Welcome to the PyMDB API!"})

@routes.route('/hardware', methods=['GET'])
def get_hardware():
    return routehelper.get_data('hardware_data')

@routes.route('/hardware/<id>', methods=['GET'])
def get_hardware_by_id(id):
    return routehelper.get_data_by_id('hardware_data', id)

@routes.route('/hardware', methods=['POST'])
def create_hardware():
    return routehelper.add_data('hardware_data')

@routes.route('/hardware/<id>', methods=['DELETE'])
def delete_hardware(id):
    return routehelper.delete_data_by_id('hardware_data', id)

@routes.route('/facilities', methods=['GET'])
def get_facilities():
    return routehelper.get_data('facilities')

@routes.route('/facilities/<id>', methods=['GET'])
def get_facility_by_id(id):
    return routehelper.get_data_by_id('facilities', id)

@routes.route('/facilities', methods=['POST'])
def create_facility():
    return routehelper.add_data('facilities')

@routes.route('/facilities/<id>', methods=['DELETE'])
def delete_facility(id):
    return routehelper.delete_data_by_id('facilities', id)

@routes.route('/operating_systems', methods=['GET'])
def get_operating_systems():
    return routehelper.get_data('operating_systems')

@routes.route('/operating_systems/<id>', methods=['GET'])
def get_operating_system_by_id(id):
    return routehelper.get_data_by_id('operating_systems', id)

@routes.route('/operating_systems', methods=['POST'])
def create_operating_system():
    return routehelper.add_data('operating_systems')

@routes.route('/operating_systems/<id>', methods=['DELETE'])
def delete_operating_system(id):
    return routehelper.delete_data_by_id('operating_systems', id)
