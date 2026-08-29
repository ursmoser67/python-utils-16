import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "host": "0.0.0.0",
    "port": 8000,
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "defaultdb",
    }
}

def merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result

def load_config(config_path: str, defaults: Dict[str, Any] = None) -> Dict[str, Any]:
    if defaults is None:
        defaults = DEFAULT_CONFIG
    config = defaults.copy()
    if os.path.isfile(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            try:
                loaded_config = json.load(file)
                if isinstance(loaded_config, dict):
                    config = merge_configs(config, loaded_config)
                else:
                    raise ValueError("Configuration file must be a JSON object")
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format in {config_path}: {e}") from e
    return config

def save_config(config: Dict[str, Any], config_path: str) -> None:
    with open(config_path, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)