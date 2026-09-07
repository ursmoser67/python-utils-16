import json
from typing import Any, Dict, Optional

def safe_json_load(data: str, default: Optional[Dict] = None) -> Dict:
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return default or {}

def flatten_dict(d: Dict, parent_key: str = '', sep: str = '_') -> Dict:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def filter_none_values(data: Dict) -> Dict:
    return {k: v for k, v in data.items() if v is not None}

def merge_configs(base: Dict, override: Dict) -> Dict:
    result = base.copy()
    for key, value in override.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_configs(result[key], value)
        else:
            result[key] = value
    return result