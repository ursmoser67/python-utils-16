class Constants:
    MAX_RETRIES = 5
    TIMEOUT = 30
    API_URL = 'https://api.example.com'

    @staticmethod
    def get_database_config():
        return {
            'host': 'localhost',
            'port': 5432,
            'user': 'admin',
            'password': 'admin'
        }

    @staticmethod
    def get_log_level():
        return 'DEBUG'

    @staticmethod
    def get_api_key():
        return 'your_api_key_here'

    @staticmethod
    def get_support_email():
        return 'support@example.com'