import numpy as np
from lab_3_task1 import yskor_free_pad as g

x0 = 2
y0 = 5
v0X = 10
t = np.arange(0, 5, 0.1)

x = x0 + v0X*t
y = y0 + v0X*t - (g*t**2)/2

print(x)
print(y)

A = np.zeros((len(x), 3))
print(A)

for i in range(0, len(x)):
    A[i, 0] = t[i]
    A[i, 1] = x[i]
    A[i, 2] = y[i]


print(A)