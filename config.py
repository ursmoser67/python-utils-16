import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, custom_config_path=None):
        self.default_config_path = default_config_path
        self.custom_config_path = custom_config_path
        self.config = self.load_config()

    def load_config(self):
        config = self.load_default_config()
        if self.custom_config_path:
            custom_config = self.load_custom_config()
            config.update(custom_config)
        return config

    def load_default_config(self):
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def load_custom_config(self):
        if not os.path.exists(self.custom_config_path):
            return {}
        with open(self.custom_config_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        return self.config.get(key, default)