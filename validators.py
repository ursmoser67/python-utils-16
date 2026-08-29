import re

def is_valid_email(email: str) -> bool:
    if not isinstance(email, str) or not email:
        return False
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def is_valid_url(url: str) -> bool:
    if not isinstance(url, str) or not url:
        return False
    pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/.*)?$"
    return re.match(pattern, url) is not None

def is_valid_phone(phone: str) -> bool:
    if not isinstance(phone, str) or not phone:
        return False
    cleaned = re.sub(r"[\s-]", "", phone)
    return bool(re.match(r"^\+?\d{10,15}$", cleaned))

def is_valid_age(age: int) -> bool:
    if not isinstance(age, int):
        return False
    return 0 <= age <= 120

def is_non_empty_string(value: str) -> bool:
    return isinstance(value, str) and bool(value.strip())

def is_positive_number(value: float) -> bool:
    if not isinstance(value, (int, float)):
        return False
    return value > 0

def is_in_range(value: float, min_val: float, max_val: float) -> bool:
    if not all(isinstance(x, (int, float)) for x in (value, min_val, max_val)):
        return False
    return min_val <= value <= max_val