import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, user_config_path):
        self.default_config_path = default_config_path
        self.user_config_path = user_config_path
        self.config = self.load_config()

    def load_config(self):
        default_config = self.load_json(self.default_config_path)
        user_config = self.load_json(self.user_config_path)
        return {**default_config, **user_config}

    def load_json(self, path):
        if not os.path.exists(path):
            return {}
        with open(path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)