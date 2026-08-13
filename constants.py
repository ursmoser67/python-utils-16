class Constants:
    MAX_RETRIES = 5
    TIMEOUT = 30
    ERROR_MESSAGES = {
        'not_found': 'Resource not found',
        'unauthorized': 'Unauthorized access',
        'server_error': 'Internal server error'
    }

    @staticmethod
    def get_error_message(key):
        return Constants.ERROR_MESSAGES.get(key, 'Unknown error')