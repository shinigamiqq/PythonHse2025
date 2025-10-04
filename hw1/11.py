def tribonacci_generator():
    a, b, c = 0, 1, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c

from sys import stdin
exec('\n'.join(stdin))

