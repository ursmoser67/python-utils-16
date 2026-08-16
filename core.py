import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        return [self._transform(item) for item in self.data]

    def _transform(self, item):
        return item.upper()  # Example transformation

class DataHandler:
    def __init__(self, processor):
        self.processor = processor

    def handle(self):
        processed = self.processor.process_data()
        return json.dumps(processed)

if __name__ == '__main__':
    data = ['foo', 'bar', 'baz']
    processor = DataProcessor(data)
    handler = DataHandler(processor)
    result = handler.handle()
    print(result)