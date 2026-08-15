import json

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.config = self.default_config.copy()

    def load(self, filepath):
        try:
            with open(filepath, 'r') as file:
                user_config = json.load(file)
            self.config.update(user_config)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON in configuration file')

    def get(self, key, default=None):
        return self.config.get(key, default)

    def all(self):
        return self.config