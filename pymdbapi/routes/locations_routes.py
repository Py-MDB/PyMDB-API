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
routes = Blueprint('locations_routes', __name__)


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

@routes.route('/regions', methods=['GET'])
@authenticate(required_privilege=1)
def get_regions():
    return routehelper.get_data('regions')

@routes.route('/regions/<id>', methods=['GET'])
@authenticate(required_privilege=1)
def get_region_by_id(id):
    return routehelper.get_data_by_id('regions', id)

@routes.route('/regions', methods=['POST'])
@authenticate(required_privilege=3)
def create_region():
    return routehelper.upsert_data('regions')

@routes.route('/regions/<id>', methods=['DELETE'])
@authenticate(required_privilege=4)
def delete_region(id):
    return routehelper.delete_data_by_id('regions', id)

@routes.route('/regions/<id>', methods=['PUT'])
@authenticate(required_privilege=3)
def upsert_region_by_id(id):
    return routehelper.upsert_data('regions', id)

@routes.route('/regions/<id>/link-facilities', methods=['POST'])
@authenticate(required_privilege=3)
def link_facilities_to_region(id):
    return routehelper.link_related_items('regions', id, 'facilities', 'facilities', 'region')
