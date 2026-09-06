from typing import Any, Dict, Generator, Iterable, List


def chunk_iterable(iterable: Iterable[Any], size: int) -> Generator[List[Any], None, None]:
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def flatten(iterable: Iterable[Any]) -> Generator[Any, None, None]:
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item


def deep_merge(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
