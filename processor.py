from typing import Any, Callable, Iterable, Optional


def batch_process(data: Iterable[Any], func: Callable[[Any], Any], chunk_size: int = 100) -> list[Any]:
    results = []
    batch = []
    for item in data:
        batch.append(item)
        if len(batch) >= chunk_size:
            results.extend(map(func, batch))
            batch = []
    if batch:
        results.extend(map(func, batch))
    return results


def deep_get(data: dict[str, Any], path: str, default: Any = None) -> Any:
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data


def flatten(items: Iterable[Any]) -> list[Any]:
    flat_list = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


def sanitize_dict(data: dict[str, Any], keys: Optional[Iterable[str]] = None) -> dict[str, Any]:
    if keys is None:
        return {k: v for k, v in data.items() if v is not None}
    return {k: v for k, v in data.items() if k in keys and v is not None}