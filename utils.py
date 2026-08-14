import json

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def deduplicate_list(lst):
    return list(set(lst))


def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]