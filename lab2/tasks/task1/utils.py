import time
from functools import wraps
import asyncio

from lab2.tasks.task1.src.consts import MAX_NUMBER


def timer_decorator(message):
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = await func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"Метод: {message}")
            print(f"Результат: {result}")
            print(f"Затрачено: {end_time - start_time:.10f} сек")
            return result
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            print(f"Метод: {message}")
            print(f"Результат: {result}")
            print(f"Затрачено: {end_time - start_time:.10f} сек")
            return result
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return sync_wrapper
    return decorator

def get_end_index(i, chunk_size, num):
    if i < num - 1:
        return (i + 1) * chunk_size + 1
    return MAX_NUMBER + 1
