import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, backoff_factor=0.3):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                raise e