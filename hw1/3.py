def interesting_trunc(array: list) -> list:
    for i in range(len(array)):
        if isinstance(array[i], str):
            array[i] = array[i].lower()[0:5]

    return array

from sys import stdin
exec('\n'.join(stdin))
