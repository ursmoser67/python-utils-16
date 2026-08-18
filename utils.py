import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def get_unique_elements(lst):
    return list(set(lst))