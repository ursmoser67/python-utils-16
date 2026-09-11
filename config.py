import json
import os
from pathlib import Path
from typing import Any, Dict, Union


class ConfigLoader:
    def __init__(self, defaults: Dict[str, Any] | None = None):
        self._defaults = defaults or {}
        self._config: Dict[str, Any] = dict(self._defaults)

    def load_from_dict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        self._config = {**self._defaults, **data}
        return self._config

    def load_from_json(self, path: Union[str, Path]) -> Dict[str, Any]:
        file_path = Path(path)
        if not file_path.exists():
            self._config = dict(self._defaults)
            return self._config
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return self.load_from_dict(data)

    def load_from_env(self, prefix: str = "") -> Dict[str, Any]:
        config = dict(self._defaults)
        for key, default_val in self._defaults.items():
            env_key = f"{prefix}{key}".upper()
            if env_key in os.environ:
                val = os.environ[env_key]
                val_type = type(default_val)
                if val_type == bool:
                    config[key] = val.lower() in ("true", "1", "yes")
                elif val_type in (int, float):
                    config[key] = val_type(val)
                else:
                    config[key] = val
        self._config = config
        return self._config

    def get(self, key: str, default: Any = None) -> Any:
        return self._config.get(key, default)
