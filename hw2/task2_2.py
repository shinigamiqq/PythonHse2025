import itertools
import operator

n = int(input())
result = list(itertools.accumulate(itertools.chain([1], range(1, 1 + n)), operator.mul))
print(result)
