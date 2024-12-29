"""
PyMDB - Python CMDB

This file is part of the PyMDB project and is licensed under the Mozilla Public License, version 2.0 (MPL-2.0).

You may obtain a copy of the MPL-2.0 at:
https://mozilla.org/MPL/2.0/

Under the terms of this license, you are free to use, modify, and distribute this file, provided that any modifications
you make are also licensed under the MPL-2.0. For full terms and conditions, refer to the license linked above.

Author(s): Jesse Butryn (jesse@jesseb.org)
"""

from flask import Flask
from flask_cors import CORS
from pymdbapi.init_db import initialize_db
from pymdbapi.routes import register_routes

app = Flask(__name__)
CORS(app)

register_routes(app)

def main():
    initialize_db()
    app.run(host='0.0.0.0', port=5000)
    # ssl_context = ('/path/to/cert.pem', '/path/to/key.pem')
    # app.run(host='0.0.0.0', port=5000, ssl_context=ssl_context)

if __name__ == "__main__":
    main()
