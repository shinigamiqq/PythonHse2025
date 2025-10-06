import itertools


number_list = list(map(int, input().split()))
n = int(input())

result = []

for i in itertools.combinations(number_list, 2):
    if sum(i) == n:
        result.append(i)

print(result)
