class CustomError(Exception):
    pass

class NotFoundError(CustomError):
    def __init__(self, message="Not found error occurred."):
        super().__init__(message)

class ValidationError(CustomError):
    def __init__(self, field, message="Validation error occurred."):
        self.field = field
        super().__init__(f'{field}: {message}')

class DatabaseError(CustomError):
    def __init__(self, message="Database error occurred."):
        super().__init__(message)

class PermissionError(CustomError):
    def __init__(self, message="Permission denied."):
        super().__init__(message)

class TimeoutError(CustomError):
    def __init__(self, message="Operation timed out."):
        super().__init__(message)