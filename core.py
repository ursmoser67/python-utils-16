import functools
import random
import time
from typing import Any, Callable, Tuple, Type


def retry(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    allowed_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as err:
                    if attempt == max_retries:
                        raise err
                    sleep_duration = delay
                    if jitter:
                        sleep_duration += random.uniform(0, delay * 0.1)
                    time.sleep(sleep_duration)
                    delay *= backoff_factor

        return wrapper

    return decorator
