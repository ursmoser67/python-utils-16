import time

class PerformanceOptimizer:
    def __init__(self):
        self._timings = {}

    def time_execution(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self._timings[func.__name__] = end_time - start_time
            return result
        return wrapper

    def get_timings(self):
        return self._timings

optimizer = PerformanceOptimizer()

@optimizer.time_execution
def sample_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

if __name__ == '__main__':
    sample_function(100000)
    print(optimizer.get_timings())