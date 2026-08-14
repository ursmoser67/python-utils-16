def process_data(data, function):
    return [function(item) for item in data]

def filter_data(data, condition):
    return [item for item in data if condition(item)]

def transform_data(data, transformation):
    return [transformation(item) for item in data]

def aggregate_data(data, aggregation_func):
    return aggregation_func(data)

def split_data(data, chunk_size):
    return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

def extract_keys(data, keys):
    return [{key: item[key] for key in keys if key in item} for item in data]

# Example usage
if __name__ == '__main__':
    sample_data = [{'id': 1, 'value': 10}, {'id': 2, 'value': 20}, {'id': 3, 'value': 30}]
    processed = process_data(sample_data, lambda x: x['value'] * 2)
    filtered = filter_data(sample_data, lambda x: x['value'] > 15)
