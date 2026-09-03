import math
from typing import Any, Dict, List, Optional, Union


class SafeDataProcessor:
    def __init__(self, strict_mode: bool = False) -> None:
        self.strict_mode = strict_mode

    def safe_divide(self, numerator: Union[int, float], denominator: Union[int, float], default: float = 0.0) -> float:
        try:
            if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
                raise TypeError("Inputs must be numeric")
            if math.isnan(numerator) or math.isnan(denominator):
                raise ValueError("Numeric inputs cannot be NaN")
            return float(numerator) / float(denominator)
        except (ZeroDivisionError, TypeError, ValueError) as e:
            if self.strict_mode:
                raise ValueError(f"Division failed: {e}") from e
            return default

    def extract_nested_key(self, data: Optional[Dict[str, Any]], path: List[str], default: Any = None) -> Any:
        if not isinstance(data, dict) or not path:
            return default
        curr = data
        for key in path:
            if not isinstance(curr, dict) or key not in curr:
                return default
            curr = curr[key]
        return curr

    def parse_numeric_list(self, raw_items: Optional[List[Any]]) -> List[float]:
        if raw_items is None:
            return []
        if not isinstance(raw_items, (list, tuple)):
            if self.strict_mode:
                raise TypeError("Expected list or tuple")
            return []
        results: List[float] = []
        for item in raw_items:
            try:
                if item is None or isinstance(item, bool):
                    continue
                val = float(item)
                if not math.isnan(val) and not math.isinf(val):
                    results.append(val)
            except (ValueError, TypeError):
                if self.strict_mode:
                    raise ValueError(f"Invalid numeric element: {item}")
                continue
        return results
