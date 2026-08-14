class Constants:
    MAX_RETRIES = 5
    TIMEOUT = 30
    API_URL = 'https://api.example.com'
    ERROR_MESSAGE = 'An error occurred'

    @staticmethod
    def get_default_headers():
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    @staticmethod
    def get_error_response(error_code):
        return {
            'error': error_code,
            'message': Constants.ERROR_MESSAGE
        }
