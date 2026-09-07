import functools
import time
from typing import Any, Callable, TypeVar, Iterable

T = TypeVar('T')

def retry(attempts: int = 3, delay: float = 1.0) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_ex = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_ex = e
                    time.sleep(delay)
            raise last_ex
        return wrapper
    return decorator

def chunker(data: Iterable[T], size: int) -> Iterable[list[T]]:
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def compose(*functions: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def compose2(f: Callable, g: Callable) -> Callable:
        return lambda x: f(g(x))
    return functools.reduce(compose2, functions, lambda x: x)