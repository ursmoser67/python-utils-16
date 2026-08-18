import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, default_config=None):
        self.default_config = default_config or {}
        self.config = self.default_config.copy()

    def load_config(self, filepath):
        if Path(filepath).is_file():
            with open(filepath, 'r') as file:
                self.config.update(json.load(file))

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def to_json(self):
        return json.dumps(self.config, indent=4)

if __name__ == '__main__':
    loader = ConfigLoader({'setting1': 'default1', 'setting2': 'default2'})
    loader.load_config('config.json')
    print(loader.to_json())