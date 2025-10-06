import numpy as np
import time
import matplotlib.pyplot as plt

def multiply_matrices(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

sizes = []
numpy_times = []
python_times = []

for n in range(2, 101):
    A = np.random.randint(1, 50, (n, n))
    B = np.random.randint(1, 50, (n, n))

    start_time = time.time()
    result_numpy = A @ B
    numpy_time = time.time() - start_time

    A_list = A.tolist()
    B_list = B.tolist()

    start_time = time.time()
    result_python = multiply_matrices(A_list, B_list)
    python_time = time.time() - start_time

    sizes.append(n)
    numpy_times.append(numpy_time)
    python_times.append(python_time)

    print(f"n={n}: NumPy: {numpy_time:.6f} сек, Python: {python_time:.6f} сек")

print("\nПроверка для n=5:")
A_check = np.random.randint(1, 50, (5, 5))
B_check = np.random.randint(1, 50, (5, 5))

result_numpy = A_check @ B_check
result_python = multiply_matrices(A_check.tolist(), B_check.tolist())

print("Результаты совпадают:", np.allclose(result_numpy, result_python))

plt.plot(sizes, numpy_times, label='NumPy')
plt.plot(sizes, python_times, label='Python списки')
plt.xlabel('Размер матрицы (n)')
plt.ylabel('Время (секунды)')
plt.legend()
plt.show()
