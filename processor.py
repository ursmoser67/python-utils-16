import json

class InputValidationError(Exception):
    pass

class Processor:
    def __init__(self):
        pass

    def validate_input(self, data):
        if not isinstance(data, dict):
            raise InputValidationError('Input must be a dictionary.')
        if 'name' not in data or 'age' not in data:
            raise InputValidationError('Input must contain name and age.')
        if not isinstance(data['age'], int) or data['age'] < 0:
            raise InputValidationError('Age must be a non-negative integer.')

    def process(self, data):
        self.validate_input(data)
        return json.dumps(data)

if __name__ == '__main__':
    processor = Processor()
    input_data = {'name': 'Alice', 'age': 30}
    try:
        result = processor.process(input_data)
        print(result)
    except InputValidationError as e:
        print(f'Error: {e}')