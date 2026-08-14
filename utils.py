import json
import os

def load_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def update_json(file_path, updates):
    data = load_json(file_path)
    data.update(updates)
    save_json(data, file_path)


def is_json_file(file_path):
    return file_path.endswith('.json')


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))
