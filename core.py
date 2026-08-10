import logging

class CustomError(Exception):
    pass


def divide_numbers(numerator, denominator):
    try:
        if denominator == 0:
            raise CustomError("Denominator cannot be zero")
        result = numerator / denominator
    except TypeError:
        logging.error("Invalid type: numerator and denominator must be numbers")
        raise CustomError("Invalid input types")
    except CustomError as ce:
        logging.error(ce)
        raise
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        raise CustomError("An unexpected error occurred")
    return result


def main():
    try:
        print(divide_numbers(10, 2))  # valid
        print(divide_numbers(10, 0))  # raises CustomError
        print(divide_numbers(10, 'a'))  # raises TypeError
    except CustomError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()