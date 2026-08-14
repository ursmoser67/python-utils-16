import os
import json
from typing import Any, Dict, List

def read_json_file(file_path: str) -> Dict[str, Any]:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_list_of_dicts(list_of_dicts: List[Dict[str, Any]], key: str) -> List[Any]:
    return [d[key] for d in list_of_dicts if key in d]