import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load_from_file(self, filepath):
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

# Default configuration
default_config = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'database': {
        'user': 'user',
        'password': 'pass',
        'name': 'db'
    }
}

# Usage example
if __name__ == '__main__':
    loader = ConfigLoader(default_config)
    loader.load_from_file('config.json')
    print(loader.get('host'))
    print(loader.get('database')['user'])