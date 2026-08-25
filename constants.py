"""Constants for python-utils-16 general utilities.

Defines typed constants and helper functions for accessing them.
"""

from typing import Any, Dict, List, Optional

DEFAULT_ENCODING: str = "utf-8"
DEFAULT_TIMEOUT: int = 30
MAX_RETRIES: int = 5
BUFFER_SIZE: int = 4096
LOG_FORMAT: str = "%(asctime)s - %(levelname)s - %(message)s"
SUPPORTED_LANGUAGES: List[str] = ["en", "es", "fr", "de", "it"]
API_ENDPOINTS: Dict[str, str] = {
    "users": "/api/v1/users",
    "products": "/api/v1/products",
    "orders": "/api/v1/orders",
    "auth": "/api/v1/auth",
}
ERROR_MESSAGES: Dict[int, str] = {
    400: "Bad request",
    401: "Unauthorized",
    404: "Not found",
    500: "Internal server error",
}
DEFAULT_CONFIG: Dict[str, Any] = {
    "encoding": DEFAULT_ENCODING,
    "timeout": DEFAULT_TIMEOUT,
    "retries": MAX_RETRIES,
}

def get_constant(name: str) -> Optional[Any]:
    """Get the value of a constant by its name.

    Args:
        name: Name of the constant (must be uppercase).

    Returns:
        The constant value if found, else None.
    """
    if name.isupper() and name in globals():
        return globals()[name]
    return None

def get_all_constants() -> Dict[str, Any]:
    """Retrieve all defined constants as a dictionary.

    Returns:
        Dictionary mapping constant names to their values.
    """
    return {
        name: value
        for name, value in globals().items()
        if name.isupper() and not name.startswith("_")
    }

def validate_constant(name: str, value: Any) -> bool:
    """Check if a constant exists and matches the provided value.

    Args:
        name: Name of the constant.
        value: Expected value to validate against.

    Returns:
        True if constant exists and equals value, False otherwise.
    """
    const_value = get_constant(name)
    return const_value is not None and const_value == value
