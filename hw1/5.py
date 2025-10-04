from functools import wraps
from typing import Callable


def log_plagiat_check(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Check '{args[0]}' vs '{args[1]}' -> {result}")
        return result
    return wrapper

@log_plagiat_check
def is_plagiat(word1: str, word2: str):
    set1 = set(word1.lower())
    set2 = set(word2.lower())

    return len(set2 - set1) <= 1

with open("words.txt", "r", encoding="utf-8") as f:
    for line in f:
        word1, word2 = line.strip().split()
        is_plagiat(word1, word2)
