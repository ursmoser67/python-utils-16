import os

class Config:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug = os.getenv('DEBUG', 'false').lower() == 'true'
        self.database_url = os.getenv('DATABASE_URL')
        self.secret_key = os.getenv('SECRET_KEY')

    def is_production(self):
        return self.environment == 'production'

    def is_debug(self):
        return self.debug

config = Config()