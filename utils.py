import json

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError('Input must be a dictionary')
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError('Name is required and must be a string')
    if 'age' not in data or not isinstance(data['age'], int) or data['age'] <= 0:
        raise ValueError('Age is required and must be a positive integer')

def process_data(data):
    validate_input(data)
    # Simulating some processing
    return json.dumps({'status': 'success', 'data': data})

if __name__ == '__main__':
    sample_input = {'name': 'Alice', 'age': 30}
    try:
        result = process_data(sample_input)
        print(result)
    except ValueError as e:
        print(f'Input error: {e}')