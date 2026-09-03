import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_from_dict(self, data: Dict[str, Any]) -> None:
        self._config.update(data)

    def load_from_json(self, filepath: str) -> bool:
        if not os.path.isfile(filepath):
            return False
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self._config.update(data)
                return True
        return False

    def load_from_env(self, prefix: str = "APP_") -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._config[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._config[key] = value

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()
