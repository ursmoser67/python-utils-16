import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] = None):
        self.defaults = defaults or {}

    def load_from_file(self, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return self.defaults.copy()

        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            return {**self.defaults, **data}
        except (json.JSONDecodeError, IOError):
            return self.defaults.copy()

    def load_from_env(self, prefix: str) -> Dict[str, Any]:
        config = self.defaults.copy()
        for key in config.keys():
            env_val = os.getenv(f"{prefix}_{key.upper()}")
            if env_val is not None:
                config[key] = env_val
        return config

def get_config(file_path: str, defaults: Dict[str, Any]) -> Dict[str, Any]:
    loader = ConfigLoader(defaults)
    config = loader.load_from_file(file_path)
    config.update(loader.load_from_env("APP"))
    return config