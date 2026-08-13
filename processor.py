import json
from validators import validate_input

def process_data(data):
    if not validate_input(data):
        raise ValueError('Invalid input data')
    # processing logic here
    result = data['value'] * 2
    return result

def main_loop():
    while True:
        try:
            user_input = input('Enter data (JSON): ')
            data = json.loads(user_input)
            result = process_data(data)
            print(f'Result: {result}')
        except (ValueError, json.JSONDecodeError) as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main_loop()