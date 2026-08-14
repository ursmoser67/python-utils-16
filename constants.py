from typing import Final

# Constants for application use

API_URL: Final[str] = "https://api.example.com"
TIMEOUT: Final[int] = 30
RETRY_LIMIT: Final[int] = 5
MAX_CONNECTIONS: Final[int] = 100

STATUS_CODES: Final[dict[int, str]] = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error"
}