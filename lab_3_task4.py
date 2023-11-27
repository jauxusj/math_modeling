import numpy as np

N = int(input('Введине кол-во строк: '))
M = int(input('Введине кол-во стобцов: '))

A = np.zeros((N, M))
print(A)


for i in range(0, N):
    for j in range(0, M):
           A[i, j] = np.sin(N * (i+1) + M * (j+1))
           if A[i, j] < 0:
               A[i, j] = 0

print(A)
