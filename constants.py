class Constants:
    MAX_CONNECTIONS = 100
    TIMEOUT = 30  # in seconds
    DEFAULT_RETRY_ATTEMPTS = 3
    BASE_URL = 'https://api.example.com'

    @staticmethod
    def get_connection_limit(limit):
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError('Connection limit must be a positive integer')
        return min(limit, Constants.MAX_CONNECTIONS)

    @staticmethod
    def get_timeout(timeout):
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            raise ValueError('Timeout must be a positive number')
        return timeout

    @staticmethod
    def get_retry_attempts(attempts):
        if not isinstance(attempts, int) or attempts < 0:
            raise ValueError('Retry attempts must be a non-negative integer')
        return attempts or Constants.DEFAULT_RETRY_ATTEMPTS