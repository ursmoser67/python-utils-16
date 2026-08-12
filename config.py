import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.user_config = {}

    def load(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                self.user_config = json.load(file)
        else:
            self.user_config = {}

    def get(self, key, default=None):
        return self.user_config.get(key, self.default_config.get(key, default))

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.user_config[key] = value

    def to_dict(self):
        config = self.default_config.copy()
        config.update(self.user_config)
        return config

# Example usage
if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(defaults)
    config_loader.load('config.json')
    print(config_loader.to_dict())