import os
from typing import Any, Dict, Optional

class ConfigManager:
    """Handles application configuration loading and access."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        self._config: Dict[str, Any] = defaults or {}

    def load_from_env(self, prefix: str = "APP_") -> None:
        """Loads environment variables starting with prefix into config."""
        for key, value in os.environ.items():
            if key.startswith(prefix):
                clean_key = key[len(prefix):].lower()
                self._config[clean_key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves configuration value by key."""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Sets configuration value for key."""
        self._config[key] = value

    @property
    def all(self) -> Dict[str, Any]:
        """Returns complete configuration dictionary."""
        return self._config.copy()