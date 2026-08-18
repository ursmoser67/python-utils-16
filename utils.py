def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return 'Error: Division by zero'
    except TypeError:
        return 'Error: Invalid input types'
    return result


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return 'Error: File not found'
    except IOError:
        return 'Error: I/O error occurred'


def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return 'Error: Invalid integer string'


def process_data(data):
    if not isinstance(data, list):
        return 'Error: Data should be a list'
    processed = []
    for item in data:
        if isinstance(item, int):
            processed.append(item ** 2)
        else:
            return 'Error: All items must be integers'
    return processed