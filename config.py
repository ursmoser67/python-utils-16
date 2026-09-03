import json
import os
from typing import Any, Dict, Optional


class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None):
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def load_dict(self, data: Dict[str, Any]) -> "ConfigLoader":
        self._deep_merge(self._config, data)
        return self

    def load_json(self, filepath: str) -> "ConfigLoader":
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.load_dict(data)
        return self

    def load_env(self, prefix: str = "") -> "ConfigLoader":
        for key, value in os.environ.items():
            if prefix and not key.startswith(prefix):
                continue
            config_key = key[len(prefix):].lower()
            if config_key:
                self._set_nested(config_key.split("__"), value)
        return self

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        val = self._config
        for k in keys:
            if isinstance(val, dict) and k in val:
                val = val[k]
            else:
                return default
        return val

    def to_dict(self) -> Dict[str, Any]:
        return self._config.copy()

    def _deep_merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        for k, v in update.items():
            if isinstance(v, dict) and k in base and isinstance(base[k], dict):
                self._deep_merge(base[k], v)
            else:
                base[k] = v

    def _set_nested(self, path: list, value: Any) -> None:
        curr = self._config
        for k in path[:-1]:
            curr = curr.setdefault(k, {})
        curr[path[-1]] = value
