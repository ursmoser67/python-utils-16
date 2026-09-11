from itertools import chain, islice
from typing import Any, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


class FastRecord:
    __slots__ = ("id", "payload", "tags")

    def __init__(self, id: int, payload: Any, tags: tuple) -> None:
        self.id = id
        self.payload = payload
        self.tags = tags


def chunk_iterable(iterable: Iterable[T], size: int) -> Iterator[List[T]]:
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero")
    iterator = iter(iterable)
    while chunk := list(islice(iterator, size)):
        yield chunk


def flatten_iterable(iterable: Iterable[Iterable[T]]) -> Iterator[T]:
    return chain.from_iterable(iterable)
