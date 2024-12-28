import os
import importlib

def register_routes(app):
    routes_dir = os.path.dirname(__file__)
    for filename in os.listdir(routes_dir):
        if filename.endswith('_routes.py'):
            module_name = f'pymdbapi.routes.{filename[:-3]}'
            module = importlib.import_module(module_name)
            app.register_blueprint(module.routes)
