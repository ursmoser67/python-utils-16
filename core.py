import sys

def validate_not_empty(value):
    if value is None or str(value).strip() == "":
        return False
    return True

def validate_is_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False

def validate_positive(value):
    num = int(value)
    if num <= 0:
        return False
    return True

def validate_upper_limit(value, limit):
    num = int(value)
    if num > limit:
        return False
    return True

def validate_input(raw):
    if not validate_not_empty(raw):
        return False, "empty"
    if not validate_is_integer(raw):
        return False, "not integer"
    if not validate_positive(raw):
        return False, "not positive"
    if not validate_upper_limit(raw, 100):
        return False, "too large"
    return True, int(raw)

def transform_data(value):
    doubled = value * 2
    adjusted = doubled - 1
    return adjusted

def main_processing_loop(data_items):
    valid_count = 0
    results = []
    for item in data_items:
        valid, info = validate_input(item)
        if valid:
            transformed = transform_data(info)
            results.append(transformed)
            valid_count += 1
        else:
            results.append(info)
    return results, valid_count

def run_processor():
    inputs = ["5", 10, "abc", "-1", "50", "200", "0", "25", None, "100"]
    processed, count = main_processing_loop(inputs)
    for p in processed:
        print(p)
    print("Valid items:", count)

if __name__ == "__main__":
    run_processor()