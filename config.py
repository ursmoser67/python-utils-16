import json
import os

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = self.default_config.copy()

    def load_from_file(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                file_config = json.load(file)
                self.config.update(file_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def get_all(self):
        return self.config

if __name__ == '__main__':
    defaults = {'host': 'localhost', 'port': 8080}
    config_loader = ConfigLoader(defaults)
    config_loader.load_from_file('config.json')
    print(config_loader.get_all())