import json


def process_data(data):
    if not isinstance(data, list):
        raise ValueError('Input must be a list.')
    return [d * 2 for d in data if isinstance(d, (int, float))]


def validate_input(data):
    if not isinstance(data, list):
        return False
    return all(isinstance(d, (int, float)) for d in data)


def main():
    input_data = json.loads(input('Enter a list of numbers: '))
    if validate_input(input_data):
        result = process_data(input_data)
        print('Processed result:', result)
    else:
        print('Invalid input. Please provide a list of numbers.')


if __name__ == '__main__':
    main()