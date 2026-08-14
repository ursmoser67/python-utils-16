import os

class Config:
    def __init__(self):
        self.env = self.get_env_variable('ENV', 'development')
        self.debug = self.get_env_variable('DEBUG', 'False') == 'True'
        self.database_url = self.get_env_variable('DATABASE_URL')

    @staticmethod
    def get_env_variable(var_name, default=None):
        return os.environ.get(var_name, default)

config = Config()