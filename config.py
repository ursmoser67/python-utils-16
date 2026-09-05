import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union


class Config:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._data: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_dict(self, data: Dict[str, Any]) -> None:
        self._deep_update(self._data, data)

    def load_json(self, filepath: Union[str, Path]) -> bool:
        path = Path(filepath)
        if not path.is_file():
            return False
        with open(path, "r", encoding="utf-8") as f:
            self.load_dict(json.load(f))
        return True

    def load_env(self, prefix: str = "APP_") -> None:
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self._data[config_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        parts = key.split(".")
        current = self._data
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
        return current

    def _deep_update(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
        for key, value in source.items():
            if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                self._deep_update(target[key], value)
            else:
                target[key] = value

    def as_dict(self) -> Dict[str, Any]:
        return self._data.copy()
