import numpy as np 
from lab_3_task4 import A
from lab_3_task4 import N


for i in range(0, N):
    s = A[i , 0] 
    A[i , 0] = A[i, 1]
    A[i, 1] = s
print(A)


