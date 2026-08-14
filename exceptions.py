class DataError(Exception):
    pass

class NotFoundError(DataError):
    def __init__(self, message="Data not found."):
        super().__init__(message)

class ValidationError(DataError):
    def __init__(self, field, message="Invalid value."):
        self.field = field
        self.message = message
        super().__init__(f'{field}: {message}')

class DuplicateEntryError(DataError):
    def __init__(self, entry):
        self.entry = entry
        super().__init__(f'Duplicate entry found: {entry}')
