import json

class CustomError(Exception):
    pass

def safe_json_loads(data):
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise CustomError('Invalid JSON format')
    except TypeError:
        raise CustomError('Data must be a string or bytes')


def divide_numbers(numerator, denominator):
    if denominator == 0:
        raise CustomError('Division by zero is undefined')
    return numerator / denominator


def fetch_data_from_api(url):
    if not isinstance(url, str):
        raise CustomError('URL must be a string')
    if not url.startswith('http'):
        raise CustomError('Invalid URL format')
    # Simulated fetch operation
    return {'data': 'sample data'}


def main():
    try:
        data = safe_json_loads('{"key": "value"}')
        result = divide_numbers(10, 0)
        api_response = fetch_data_from_api('http://api.example.com')
    except CustomError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()