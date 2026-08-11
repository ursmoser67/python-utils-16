import json

class InputValidationError(Exception):
    pass

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def validate_input(self):
        if not isinstance(self.data, dict):
            raise InputValidationError('Input must be a dictionary.')
        if 'name' not in self.data or not isinstance(self.data['name'], str):
            raise InputValidationError('Missing or invalid name.')
        if 'age' not in self.data or not isinstance(self.data['age'], int):
            raise InputValidationError('Missing or invalid age.')
        return True

    def process_data(self):
        try:
            self.validate_input()
            # Simulating data processing
            return json.dumps({'status': 'success', 'data': self.data})
        except InputValidationError as e:
            return json.dumps({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    sample_data = {'name': 'Alice', 'age': 30}
    processor = DataProcessor(sample_data)
    result = processor.process_data()
    print(result)