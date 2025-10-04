def cyclic_shift(s):
    yield s
    shifted_s = s[1:] + s[0]
    while shifted_s != s:
        yield shifted_s
        new_s = shifted_s
        shifted_s = new_s[1:] + new_s[0]


from sys import stdin
exec('\n'.join(stdin))

