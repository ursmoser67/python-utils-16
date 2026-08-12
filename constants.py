API_BASE_URL = "https://api.example.com/v1"
TIMEOUT = 30
MAX_RETRIES = 5
DEFAULT_LANGUAGE = "en"
SUPPORTED_FORMATS = ["json", "xml"]
SUCCESS_CODE = 200
NOT_FOUND_CODE = 404
SERVER_ERROR_CODE = 500
ERROR_MESSAGES = {
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}

def is_valid_format(format_name):
    return format_name in SUPPORTED_FORMATS

def get_error_message(code):
    return ERROR_MESSAGES.get(code, "Unknown Error")
