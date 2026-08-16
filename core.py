import time

class PerformanceOptimizer:
    def __init__(self):
        self.execution_times = []

    def measure_time(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            self.execution_times.append(end_time - start_time)
            return result
        return wrapper

    def get_average_time(self):
        if not self.execution_times:
            return 0
        return sum(self.execution_times) / len(self.execution_times)

# Example usage
@PerformanceOptimizer().measure_time
def sample_function(x):
    time.sleep(x)
    return x

if __name__ == '__main__':
    for i in range(1, 4):
        sample_function(i)
    optimizer = PerformanceOptimizer()
    print(f'Average execution time: {optimizer.get_average_time()} seconds')