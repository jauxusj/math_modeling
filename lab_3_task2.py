import numpy as np
from lab_3_task1 import yskor_free_pad as g

h = 100
b = 30
a = np.pi/3

skor = (g*h*np.tan(b)**2)/(2*np.cos(a)**2*(1-np.tan(b)*np.tan(a)))
v = skor**0.5
print(v)