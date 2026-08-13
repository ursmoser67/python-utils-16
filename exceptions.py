class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message="Not Found Error occurred."):
        super().__init__(message)

class ValidationError(CustomError):
    def __init__(self, message="Validation Error occurred."):
        super().__init__(message)

class PermissionDeniedError(CustomError):
    def __init__(self, message="Permission Denied Error occurred."):
        super().__init__(message)

class ConfigurationError(CustomError):
    def __init__(self, message="Configuration Error occurred."):
        super().__init__(message)

class DatabaseError(CustomError):
    def __init__(self, message="Database Error occurred."):
        super().__init__(message)