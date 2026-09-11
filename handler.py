import logging

class ValidationError(Exception):
    pass

def validate_payload(data):
    if not isinstance(data, dict):
        raise ValidationError("payload must be a dictionary")
    if "id" not in data or not isinstance(data["id"], int):
        raise ValidationError("payload missing valid integer id")
    return True

def process_items(items):
    processed = []
    for item in items:
        try:
            if validate_payload(item):
                result = item["id"] * 2
                processed.append(result)
        except (ValidationError, KeyError) as e:
            logging.error(f"skipping invalid item: {e}")
            continue
    return processed

def main_loop(data_stream):
    logging.basicConfig(level=logging.INFO)
    while True:
        try:
            chunk = next(data_stream)
            results = process_items(chunk)
            logging.info(f"processed {len(results)} items")
        except StopIteration:
            break
        except Exception as e:
            logging.critical(f"stream failure: {e}")
            break