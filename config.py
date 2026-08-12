import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.config = self.default_config.copy()

    def load(self, path):
        try:
            with open(path, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in config file: {path}")

    def get(self, key, default=None):
        return self.config.get(key, default)

    def all(self):
        return self.config

# Example of providing default configuration
default_config = {
    'host': 'localhost',
    'port': 8080,
    'debug': False
}

loader = ConfigLoader(default_config)
loader.load('config.json')
