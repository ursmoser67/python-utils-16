class BaseUtilsError(Exception):
    """Base exception for python-utils-16."""


class ConfigurationError(BaseUtilsError):
    """Raised when configuration is invalid."""


class ValidationError(BaseUtilsError):
    """Raised when data validation fails."""


class ProcessingError(BaseUtilsError):
    """Raised when data processing fails."""


def raise_if_none(value, name="Value"):
    if value is None:
        raise ValidationError(f"{name} cannot be None")
    return value


def validate_range(value, min_val, max_val, name="Value"):
    if not (min_val <= value <= max_val):
        raise ValidationError(f"{name} must be between {min_val} and {max_val}")
    return value


def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        raise ProcessingError(f"Execution failed: {str(e)}") from e