import json
import os

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config if default_config else {}

    def load(self, filepath):
        if not os.path.isfile(filepath):
            return self.default_config
        with open(filepath, 'r') as config_file:
            return {**self.default_config, **json.load(config_file)}

# Example usage:
if __name__ == '__main__':
    default_settings = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(default_settings)
    config = config_loader.load('config.json')
    print(config)