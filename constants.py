import json
import os

DEFAULT_CONFIG = {
    'app_name': 'MyApp',
    'version': '1.0.0',
    'debug': False,
    'database': {
        'host': 'localhost',
        'port': 5432,
        'user': 'user',
        'password': 'pass',
        'dbname': 'app_db'
    }
}

def load_config(file_path):
    if not os.path.exists(file_path):
        return DEFAULT_CONFIG
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return {**DEFAULT_CONFIG, **config}
