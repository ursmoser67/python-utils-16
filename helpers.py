import os
from typing import Any, List, Optional

def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def flatten(items: List[Any]) -> List[Any]:
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def get_env_var(key: str, default: Optional[str] = None) -> str:
    return os.environ.get(key, default or "")

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    return [data[i:i + size] for i in range(0, len(data), size)]

def clean_dict(data: dict) -> dict:
    return {k: v for k, v in data.items() if v is not None}