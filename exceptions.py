class UtilityError(Exception):
    """Base exception for utility operations."""

class ConfigurationError(UtilityError):
    """Raised when config parameters are invalid."""

class ValidationError(UtilityError):
    """Raised when data validation fails."""

class ProcessingError(UtilityError):
    """Raised during core processing failures."""

def handle_exception(e: Exception) -> None:
    """Generic handler for module exceptions."""
    if isinstance(e, UtilityError):
        print(f"Utility failure: {e}")
    else:
        print(f"Unexpected system error: {e}")

def validate_input(data: any) -> None:
    if data is None:
        raise ValidationError("input cannot be null")
    if not isinstance(data, (dict, list)):
        raise ValidationError("invalid data structure")

def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except UtilityError as e:
        handle_exception(e)
        return None
    except Exception as e:
        handle_exception(e)
        raise