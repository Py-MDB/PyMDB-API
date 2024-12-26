"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

import uuid
from pymdbapi.mongodb import PyMongoDB

def initialize_db():
    db = PyMongoDB()
    
    # Check if admin user exists
    admin_user = db.find_by_key_value('users', {'username': 'admin'})
    if not admin_user:
        admin_user_data = {
            'username': 'admin',
            'full name': 'Admin User',
            'email': 'admin@example.com',
            'privilege_level': 5,
            'tokens': [str(uuid.uuid4())]
        }
        db.insert_user(admin_user_data)
        print("Admin user created with token:", admin_user_data['tokens'][0])
    else:
        print("Admin user already exists")

    # Check if admin app token exists
    admin_app_token = db.find_by_key_value('app_tokens', {'name': 'admin_app'})
    if not admin_app_token:
        admin_app_token_data = {
            'name': 'admin_app',
            'description': 'Admin App Token',
            'privilege_level': 5,
            'token': str(uuid.uuid4())
        }
        db.insert_app_token(admin_app_token_data)
        print("Admin app token created:", admin_app_token_data['token'])
    else:
        print("Admin app token already exists")

if __name__ == "__main__":
    initialize_db()
