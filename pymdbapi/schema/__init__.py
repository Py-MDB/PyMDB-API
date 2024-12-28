import os
import importlib

class DatabaseSchema:
    def __init__(self):
        schema_dir = os.path.dirname(__file__)
        for filename in os.listdir(schema_dir):
            if filename.endswith('_schema.py'):
                module_name = filename[:-3] 
                module = importlib.import_module(f'.{module_name}', package='pymdbapi.schema')
                schema_name = f'{module_name}'
                setattr(self, schema_name, getattr(module, schema_name))
