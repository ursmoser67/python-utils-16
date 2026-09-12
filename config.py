import json
import os
from typing import Any, Dict, Optional

class ConfigurationError(Exception):
    pass

class Config:
    def __init__(self, filepath: str, defaults: Optional[Dict[str, Any]] = None):
        self.filepath = filepath
        self.defaults = defaults or {}
        self.data: Dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        if not os.path.exists(self.filepath):
            self.data = self.defaults.copy()
            return
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    self.data = self.defaults.copy()
                    return
                parsed = json.loads(content)
                if not isinstance(parsed, dict):
                    raise ConfigurationError("Configuration root must be a JSON object")
                self.data = {**self.defaults, **parsed}
        except (PermissionError, OSError) as e:
            raise ConfigurationError(f"Configuration file {self.filepath} is not accessible") from e
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Failed to parse JSON config: {e}") from e

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def get_as_type(self, key: str, expected_type: type, default: Any = None) -> Any:
        val = self.get(key, default)
        if val is None:
            return None
        try:
            return expected_type(val)
        except (ValueError, TypeError) as e:
            raise ConfigurationError(f"Key '{key}' cannot be cast to {expected_type.__name__}") from e