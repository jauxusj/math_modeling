import numpy as np
from lab_3_task1 import yskor_free_pad as g

x0 = 2
y0 = 5
v0X = 10
t = np.arange(0, 5, 0.01)

x = x0 + v0X*t
y = y0 + v0X*t - (g*t**2)/2

print(x)
print(y)