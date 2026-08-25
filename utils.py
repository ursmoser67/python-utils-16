import json
import os
from typing import Any, Dict, List, Optional


def divide_numbers(a: Any, b: Any) -> Optional[float]:
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return None
        if b == 0:
            return None
        return float(a) / float(b)
    except Exception:
        return None


def read_file_content(filepath: str) -> Optional[str]:
    try:
        if not isinstance(filepath, str) or not filepath:
            return None
        if not os.path.isfile(filepath):
            return None
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except (OSError, IOError, TypeError):
        return None


def parse_json_string(data: Any) -> Optional[Dict[str, Any]]:
    try:
        if not isinstance(data, str) or not data.strip():
            return None
        return json.loads(data)
    except (json.JSONDecodeError, TypeError, ValueError):
        return None


def filter_none_items(items: Any) -> List[Any]:
    try:
        if items is None:
            return []
        if not isinstance(items, (list, tuple)):
            return []
        return [item for item in items if item is not None]
    except Exception:
        return []


def get_value_safely(data: Any, key: str, default: Any = None) -> Any:
    try:
        if not isinstance(data, dict):
            return default
        return data.get(key, default)
    except Exception:
        return default


def calculate_average(numbers: Any) -> Optional[float]:
    try:
        if numbers is None:
            return None
        if not isinstance(numbers, (list, tuple)):
            return None
        valid_numbers = [n for n in numbers if isinstance(n, (int, float))]
        if not valid_numbers:
            return None
        return sum(valid_numbers) / len(valid_numbers)
    except Exception:
        return None
