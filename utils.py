import json

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("Expected a dictionary.")
    if 'name' not in data or not isinstance(data['name'], str):
        raise ValueError("Missing or invalid 'name'.")
    if 'age' not in data or not isinstance(data['age'], int):
        raise ValueError("Missing or invalid 'age'.")

    return True

def process_data(data):
    validate_input(data)
    response = {"status": "success", "message": f"Processed {data['name']}"}
    return json.dumps(response)

if __name__ == '__main__':
    sample_data = {"name": "John", "age": 30}
    try:
        result = process_data(sample_data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
