class ErrorMessages:
    FILE_NOT_FOUND = 'File not found'
    INVALID_INPUT = 'Invalid input'
    TIMEOUT = 'Operation timed out'

class Config:
    MAX_RETRIES = 5
    TIMEOUT_SECONDS = 30
    VALID_EXTENSIONS = ['.txt', '.csv', '.json']

def is_valid_extension(filename):
    return any(filename.endswith(ext) for ext in Config.VALID_EXTENSIONS)

def validate_file(file_path):
    if not isinstance(file_path, str):
        raise ValueError(ErrorMessages.INVALID_INPUT)
    if not is_valid_extension(file_path):
        raise ValueError(ErrorMessages.INVALID_INPUT)
    return True

def get_max_retries():
    return Config.MAX_RETRIES

def get_timeout():
    return Config.TIMEOUT_SECONDS