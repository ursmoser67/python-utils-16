import json
from typing import Any, Dict, Optional

def sanitize_data(data: Any) -> Any:
    if isinstance(data, dict):
        return {str(k): sanitize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [sanitize_data(i) for i in data]
    if isinstance(data, (str, int, float, bool, type(None))):
        return data
    return str(data)

def safe_json_load(content: str) -> Dict[str, Any]:
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return {}

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)