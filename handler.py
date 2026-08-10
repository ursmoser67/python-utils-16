import time
import requests

class NetworkError(Exception):
    pass

def retry(func, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return func()
        except requests.RequestException:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise NetworkError('Max retries reached')

def fetch_data(url):
    response = retry(lambda: requests.get(url))
    return response.json() if response.status_code == 200 else None

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except NetworkError as e:
        print(e)