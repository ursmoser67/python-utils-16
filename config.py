import json
import os
from typing import Any, Dict

class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any]):
        self._config = defaults.copy()

    def load_from_file(self, filepath: str) -> None:
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                file_data = json.load(f)
                self._config.update(file_data)

    def load_from_env(self, prefix: str = 'APP_') -> None:
        for key in self._config:
            env_key = f"{prefix}{key.upper()}"
            if env_key in os.environ:
                self._config[key] = os.environ[env_key]

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    @property
    def all(self) -> Dict[str, Any]:
        return self._config.copy()