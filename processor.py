import logging

class DataProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate_input(self, data: dict) -> bool:
        if not isinstance(data, dict):
            return False
        if 'id' not in data or not isinstance(data.get('id'), int):
            return False
        if 'value' not in data or not isinstance(data.get('value'), (int, float)):
            return False
        return True

    def process_stream(self, items: list):
        for item in items:
            try:
                if not self.validate_input(item):
                    self.logger.warning(f"skipping invalid item: {item}")
                    continue
                
                result = item['value'] * 2
                print(f"processed id {item['id']}: {result}")
            except Exception as e:
                self.logger.error(f"unexpected processing error: {e}")

if __name__ == '__main__':
    processor = DataProcessor()
    test_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 'invalid'},
        {'id': 3, 'value': 20},
        'bad_format'
    ]
    processor.process_stream(test_data)