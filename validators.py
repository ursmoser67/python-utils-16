import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    pattern = r'^[+]?\d{10,15}$'
    return bool(re.match(pattern, phone))

def is_valid_username(username: str) -> bool:
    return len(username) >= 3 and len(username) <= 30 and username.isalnum()

def validate_user_data(email: str, phone: str, username: str) -> dict:
    return {
        'email': is_valid_email(email),
        'phone': is_valid_phone(phone),
        'username': is_valid_username(username)
    }
