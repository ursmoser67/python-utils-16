import json

class ConfigLoader:
    def __init__(self, default_config):
        self.default_config = default_config
        self.config = default_config.copy()

    def load(self, filepath):
        try:
            with open(filepath, 'r') as file:
                user_config = json.load(file)
            self.config.update(user_config)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON format')

    def get(self, key, default=None):
        return self.config.get(key, default)

    def all(self):
        return self.config

# Example usage
if __name__ == '__main__':
    default_settings = {'key1': 'value1', 'key2': 'value2'}
    loader = ConfigLoader(default_settings)
    loader.load('user_config.json')
    print(loader.all())