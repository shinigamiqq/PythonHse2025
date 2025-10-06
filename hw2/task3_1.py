import numpy as np

random_numbers = np.random.randint(0, 100, 20)
print(random_numbers)
print(random_numbers.mean())
print(random_numbers.min())
print(random_numbers.max())
print(random_numbers.argmin())

A = np.arange(2, 15, 2)
B = np.array([7, 11, 17, 18, 23, 30, 45])

squarred_array = (A + B) ** 2
print(squarred_array)

indices = np.where((B > 12) & (B % 5 == 3))
print(A[indices])

print(A % 2)
print(A % 3)

b = np.random.randint(0, 100, (3, 1))
print(b)
c = np.random.randint(0, 100, (3, 3))
print(c)
x = np.linalg.solve(c, b)
print(x)
#error_case = np.linalg.solve(np.zeros(2), b)
#print(error_case)

