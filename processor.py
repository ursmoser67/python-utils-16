from typing import Any, Callable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def chunk_iterable(data: List[T], size: int) -> List[List[T]]:
    if size <= 0:
        raise ValueError("Chunk size must be positive")
    return [data[i : i + size] for i in range(0, len(data), size)]


def process_in_batches(
    items: List[T], func: Callable[[T], R], batch_size: int = 10
) -> List[R]:
    results = []
    for chunk in chunk_iterable(items, batch_size):
        results.extend([func(item) for item in chunk])
    return results


def flatten_nested_list(nested: List[List[T]]) -> List[T]:
    return [item for sublist in nested for item in sublist]


def filter_none_values(data: List[Any]) -> List[Any]:
    return [x for x in data if x is not None]
