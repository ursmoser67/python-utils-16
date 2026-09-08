import json
import os
from typing import Any, Dict, Optional, Type, TypeVar

T = TypeVar("T")


class ConfigManager:
    """Manages application configuration settings from environment or dictionaries."""

    def __init__(self, defaults: Optional[Dict[str, Any]] = None) -> None:
        """Initialize config with optional default settings."""
        self._config: Dict[str, Any] = defaults.copy() if defaults else {}

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieve a configuration value by key, checking env vars first."""
        env_val = os.getenv(key.upper())
        if env_val is not None:
            return env_val
        return self._config.get(key, default)

    def get_as(
        self, key: str, cast_type: Type[T], default: Optional[T] = None
    ) -> Optional[T]:
        """Retrieve a configuration value cast to a specific type."""
        val = self.get(key)
        if val is None:
            return default
        try:
            return cast_type(val)
        except (ValueError, TypeError):
            return default

    def set(self, key: str, value: Any) -> None:
        """Set a configuration key to a specific value."""
        self._config[key] = value

    def load_from_json(self, filepath: str) -> None:
        """Load configuration settings from a JSON file."""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self._config.update(data)
