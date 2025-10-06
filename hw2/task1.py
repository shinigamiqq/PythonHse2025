from collections.abc import Iterable


def get_consistent_object(x: list):
    for i in x:
        if isinstance(i, dict):
            yield from get_consistent_object(i.keys())
        elif isinstance(i, Iterable) and not isinstance(i, (str, bytes, dict)):
            yield from get_consistent_object(i)
        elif isinstance(i, str):
            yield from i
        else:
            yield i

print(list(get_consistent_object([1, 2, 'abc', [2, 4], {'key': 'value'}])))

