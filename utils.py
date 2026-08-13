import json
from typing import Any, Dict

def read_json(file_path: str) -> Dict[str, Any]:
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path: str, data: Dict[str, Any]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    merged = dict1.copy()
    merged.update(dict2)
    return merged


def filter_dict(data: Dict[str, Any], keys: list) -> Dict[str, Any]:
    return {key: data[key] for key in keys if key in data}