import time

class PerformanceTimer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            raise RuntimeError("Timer has not been started.")
        elapsed = time.perf_counter() - self.start_time
        self.start_time = None
        return elapsed

def optimized_function(data):
    timer = PerformanceTimer()
    timer.start()
    result = []
    for item in data:
        processed = process_item(item)
        result.append(processed)
    elapsed_time = timer.stop()
    print(f"Function executed in {elapsed_time:.4f} seconds.")
    return result

def process_item(item):
    return item * 2  # Example processing step