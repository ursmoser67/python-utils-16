import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load(self, path: str) -> Dict[str, Any]:
        config = self.defaults.copy()
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    file_data = json.load(f)
                    config.update(file_data)
            except (json.JSONDecodeError, IOError):
                pass
        return config

def get_config(path: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    loader = ConfigLoader(defaults)
    return loader.load(path)