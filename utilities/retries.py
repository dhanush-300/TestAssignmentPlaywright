# utilities/retries.py
import time
from typing import Callable, Type
from playwright.sync_api import TimeoutError

def retry(func: Callable, exceptions: tuple[Type[Exception], ...] = (Exception,), attempts: int = 3, delay: float = 1.0):
    last = None
    for attempt in range(1, attempts + 1):
        try:
            return func()
        except exceptions as e:
            last = e
            if attempt == attempts:
                raise
            time.sleep(delay)