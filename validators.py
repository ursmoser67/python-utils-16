from typing import Any, Dict, List


def validate_input(data: Dict[str, Any], required_keys: List[str]) -> None:
    """Ensures all required keys are present and values are not None."""
    for key in required_keys:
        if key not in data:
            raise ValueError(f"missing required key: {key}")
        if data[key] is None:
            raise ValueError(f"key {key} cannot be null")


def validate_numeric(value: Any, min_val: int = 0) -> int:
    """Ensures value is an integer and within bounds."""
    try:
        val = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"invalid numeric value: {value}")
    if val < min_val:
        raise ValueError(f"value {val} below minimum {min_val}")
    return val


def process_main_loop(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Validated processing loop for batch data."""
    required = ["id", "amount"]
    results = []
    for item in items:
        try:
            validate_input(item, required)
            amount = validate_numeric(item["amount"])
            results.append({"id": item["id"], "amount": amount, "status": "ok"})
        except ValueError:
            continue
    return results