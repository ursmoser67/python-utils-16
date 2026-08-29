import copy
import json
from typing import Any, Dict, List, Union

def get_nested_value(data: Any, keys: List[Union[str, int]], default: Any = None) -> Any:
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        elif isinstance(current, (list, tuple)) and isinstance(key, int) and 0 <= key < len(current):
            current = current[key]
        else:
            return default
    return current

def flatten_dict(nested_dict: Dict[str, Any], separator: str = ".") -> Dict[str, Any]:
    flat_dict: Dict[str, Any] = {}
    def flatten_helper(d: Dict[str, Any], parent: str = "") -> None:
        for key, value in d.items():
            new_key = f"{parent}{separator}{key}" if parent else key
            if isinstance(value, dict):
                flatten_helper(value, new_key)
            else:
                flat_dict[new_key] = value
    flatten_helper(nested_dict)
    return flat_dict

def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    result = copy.deepcopy(dict1)
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = copy.deepcopy(value)
    return result

def safe_load_json(json_str: str) -> Union[Dict[str, Any], None]:
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError, ValueError):
        return None

def convert_keys_to_str(data: Any) -> Any:
    if isinstance(data, dict):
        return {str(k): convert_keys_to_str(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_keys_to_str(item) for item in data]
    else:
        return data