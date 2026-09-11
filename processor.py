from typing import List, Optional, Any, Callable

class DataProcessor:
    """Utility class for processing collections of data."""

    def __init__(self, items: Optional[List[Any]] = None) -> None:
        """Initialize processor with optional data list."""
        self.items: List[Any] = items or []

    def filter_data(self, predicate: Callable[[Any], bool]) -> List[Any]:
        """Filter items based on a provided predicate function."""
        return [item for item in self.items if predicate(item)]

    def transform_data(self, func: Callable[[Any], Any]) -> List[Any]:
        """Apply a transformation function to all stored items."""
        self.items = [func(item) for item in self.items]
        return self.items

    def clear(self) -> None:
        """Remove all items from the processor."""
        self.items.clear()

    def __len__(self) -> int:
        """Return the current count of items."""
        return len(self.items)