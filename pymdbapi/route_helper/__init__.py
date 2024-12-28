import os
import importlib

class RouteHelper:
    def __init__(self):
        helper_dir = os.path.dirname(__file__)
        for filename in os.listdir(helper_dir):
            if filename.endswith('_helper.py'):
                module_name = filename[:-3]
                module = importlib.import_module(f'pymdbapi.route_helper.{module_name}')
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if callable(attr) and not attr_name.startswith("__"):
                        setattr(self, attr_name, attr)
