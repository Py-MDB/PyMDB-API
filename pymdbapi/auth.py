"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import request, jsonify
from functools import wraps
from pymdbapi.mongodb import PyMongoDB

db = PyMongoDB()

def authenticate(required_privilege=1):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user_token = request.headers.get('User-Token')
            app_token = request.headers.get('App-Token')
            
            if not user_token or not app_token:
                return jsonify({"error": "User-Token and App-Token are required"}), 401
            
            user = db.find_by_key_value('users', {'tokens': user_token})
            app = db.find_by_key_value('app_tokens', {'token': app_token})
            
            if not user or not app:
                return jsonify({"error": "Invalid User-Token or App-Token"}), 401
            
            user_privilege = user[0].get('privilege_level', 'user')
            app_privilege = app[0].get('privilege_level', 'user')
            
            if user_privilege < required_privilege or app_privilege < required_privilege:
                return jsonify({"error": "Insufficient privileges"}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator
