from typing import Any, List, Optional

class DataProcessor:
    def __init__(self, data: Optional[List[Any]] = None):
        self.data = data or []

    def process(self) -> List[Any]:
        return [self._sanitize(item) for item in self.data if item is not None]

    @staticmethod
    def _sanitize(item: Any) -> Any:
        if isinstance(item, str):
            return item.strip().lower()
        return item

    def add_item(self, item: Any) -> None:
        if item not in self.data:
            self.data.append(item)

    def clear(self) -> None:
        self.data.clear()

    @property
    def is_empty(self) -> bool:
        return len(self.data) == 0