import requests
import time
from functools import wraps


def retry(times=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as e:
                    if attempt < times - 1:
                        time.sleep(delay)
                        delay *= backoff
                    else:
                        raise e
        return wrapper
    return decorator


@retry(times=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()