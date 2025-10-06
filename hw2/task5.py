from typing import Callable
import time
from functools import wraps

def limit_calls():
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(3):
                res = func(*args, **kwargs)
                print(f"Вызов {i+1}: result = {res}")
                if i < 2:
                    time.sleep(2)
            return res
        return inner
    return wrapper

@limit_calls()
def my_func():
    return 124

print("Запуск функции")
my_func()
