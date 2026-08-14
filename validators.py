import re

def validate_email(email: str) -> bool:
    pattern = r'^[\w\.]+@[\w\.]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))

def validate_username(username: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.-]+$
    return bool(re.match(pattern, username))

def validate_password(password: str) -> bool:
    return len(password) >= 8 and any(char.isdigit() for char in password)
