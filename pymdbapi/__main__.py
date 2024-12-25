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
from pymdbapi.routes import routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)

def main():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
