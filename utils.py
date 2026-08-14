import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, backoff_factor=1):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise e
            time.sleep(backoff_factor * (2 ** (attempts - 1)))
