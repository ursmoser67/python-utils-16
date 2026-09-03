from typing import Any, Dict, Tuple

class FastPathResolver:
    __slots__ = ('_cache', '_limit')

    def __init__(self, cache_limit: int = 1000) -> None:
        self._cache: Dict[str, Tuple[str, ...]] = {}
        self._limit: int = cache_limit

    def _parse_path(self, path: str) -> Tuple[str, ...]:
        if path in self._cache:
            return self._cache[path]
        
        result = tuple(path.split('.'))
        if len(self._cache) < self._limit:
            self._cache[path] = result
        return result

    def get(self, target: Any, path: str, default: Any = None) -> Any:
        if not path:
            return target
        
        keys = self._parse_path(path)
        current = target
        
        try:
            for key in keys:
                if isinstance(current, dict):
                    current = current[key]
                elif isinstance(current, (list, tuple)):
                    current = current[int(key)]
                else:
                    current = getattr(current, key)
        except (KeyError, IndexError, ValueError, AttributeError):
            return default
            
        return current
