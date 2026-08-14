import json

class InputValidationError(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        raise InputValidationError('Data must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise InputValidationError('Name is required and must be a string')
    if 'age' not in data or not isinstance(data['age'], int):
        raise InputValidationError('Age is required and must be an integer')
    return {'status': 'success', 'data': data}

def main_loop(inputs):
    results = []
    for item in inputs:
        try:
            result = process_data(item)
            results.append(result)
        except InputValidationError as e:
            results.append({'status': 'error', 'message': str(e)})
    return json.dumps(results)

if __name__ == '__main__':
    sample_inputs = [
        {'name': 'Alice', 'age': 30},
        {'name': 123, 'age': 'thirty'},
        {'name': 'Bob', 'age': 25}
    ]
    output = main_loop(sample_inputs)
    print(output)