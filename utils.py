import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=4, delay=1.0, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            m_tries, m_delay = tries, delay
            while m_tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning("Request failed: %s. Retrying in %s seconds...", e, m_delay)
                    time.sleep(m_delay)
                    m_tries -= 1
                    m_delay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator