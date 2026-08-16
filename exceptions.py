class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NotFoundError(CustomError):
    def __init__(self, resource):
        message = f'{resource} not found'
        super().__init__(message)

class ValidationError(CustomError):
    def __init__(self, field, issue):
        message = f'Validation error on {field}: {issue}'
        super().__init__(message)

class OperationFailedError(CustomError):
    def __init__(self, operation):
        message = f'Operation failed: {operation}'
        super().__init__(message)