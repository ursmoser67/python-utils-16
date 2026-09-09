from typing import Any, Optional, Union

def validate_email(email: str) -> bool:
    """Validate standard email address format."""
    if not isinstance(email, str) or "@" not in email:
        return False
    return email.count("@") == 1 and "." in email.split("@")[1]

def validate_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
    """Check if numeric value is within bounds."""
    return min_val <= value <= max_val

def validate_required(data: Any, field: str) -> bool:
    """Verify presence of field in dictionary."""
    if not isinstance(data, dict):
        return False
    return field in data and data[field] is not None

def validate_length(text: str, min_len: int, max_len: Optional[int] = None) -> bool:
    """Ensure string length fits specified constraints."""
    length = len(text)
    if max_len is None:
        return length >= min_len
    return min_len <= length <= max_len