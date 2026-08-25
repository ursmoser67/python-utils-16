import os
import json
from typing import Any, Dict, Optional

DEFAULTS: Dict[str, Any] = {
    "debug": False,
    "log_level": "INFO",
    "max_retries": 3,
    "timeout": 30,
}

class ConfigLoader:
    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self.defaults = defaults or DEFAULTS
        self.config: Dict[str, Any] = self.defaults.copy()

    def load(
        self,
        config_dict: Optional[Dict[str, Any]] = None,
        file_path: Optional[str] = None,
        env_prefix: Optional[str] = "APP_",
    ) -> Dict[str, Any]:
        if config_dict is not None:
            self.config.update(config_dict)
        if file_path is not None and os.path.isfile(file_path):
            with open(file_path, encoding="utf-8") as f:
                file_config: Dict[str, Any] = json.load(f)
            self.config.update(file_config)
        if env_prefix:
            for key, value in os.environ.items():
                if key.startswith(env_prefix):
                    cfg_key = key[len(env_prefix):].lower()
                    if cfg_key in self.config:
                        self.config[cfg_key] = self._parse_value(value)
        return self.config

    def _parse_value(self, value: str) -> Any:
        lower = value.lower()
        if lower in {"true", "1", "yes"}:
            return True
        if lower in {"false", "0", "no"}:
            return False
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)