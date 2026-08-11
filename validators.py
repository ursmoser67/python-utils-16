def validate_email(email):
    if not isinstance(email, str):
        raise ValueError("Email must be a string")
    if '@' not in email or '.' not in email:
        raise ValueError("Invalid email format")
    return True


def validate_age(age):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True


def validate_positive_number(number):
    if not isinstance(number, (int, float)):
        raise ValueError("Number must be an integer or float")
    if number <= 0:
        raise ValueError("Number must be positive")
    return True
