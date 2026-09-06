import json
from typing import Any, Dict, List, Optional
from pathlib import Path

def read_json(path: str) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(path: str, data: Any) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def chunk_list(data: List[Any], size: int) -> List[List[Any]]:
    return [data[i:i + size] for i in range(0, len(data), size)]

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def get_env_or_default(key: str, default: Any, env_vars: Optional[Dict[str, str]] = None) -> Any:
    import os
    source = env_vars or os.environ
    return source.get(key, default)