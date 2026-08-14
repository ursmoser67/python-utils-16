import json
import os

class ConfigLoader:
    def __init__(self, defaults=None):
        self.defaults = defaults or {}
        self.config = self.defaults.copy()

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def all(self):
        return self.config

# Example defaults
def create_default_config():
    return {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }

if __name__ == '__main__':
    loader = ConfigLoader(create_default_config())
    loader.load('config.json')
    print(loader.all())