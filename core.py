import time
from typing import List, Any, Callable

class BatchProcessor:
    __slots__ = ("batch_size", "timeout", "callback", "_buffer", "_last_flush")

    def __init__(self, batch_size: int, timeout: float, callback: Callable[[List[Any]], None]):
        self.batch_size = batch_size
        self.timeout = timeout
        self.callback = callback
        self._buffer: List[Any] = []
        self._last_flush = time.time()

    def add(self, item: Any) -> None:
        self._buffer.append(item)
        if len(self._buffer) >= self.batch_size or (time.time() - self._last_flush) >= self.timeout:
            self.flush()

    def flush(self) -> None:
        if not self._buffer:
            return
        current_batch = self._buffer
        self._buffer = []
        self._last_flush = time.time()
        self.callback(current_batch)

    def check_timeout(self) -> None:
        if self._buffer and (time.time() - self._last_flush) >= self.timeout:
            self.flush()