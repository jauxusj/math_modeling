import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('Orion.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t0 = np.linspace(np.pi,np.pi/1.9, 100)
x0 = 305 + 40*np.cos(t0)
y0 = 1125 - 175*np.sin(t0)
ax.plot(x0, y0, '-', lw=2, color='c')

t1 = np.linspace(np.pi, np.pi/1.85,100)
x1 = 475 + 175*np.cos(t1)
y1 = 950 - 100*np.sin(t1)
ax.plot(x1, y1, '-', lw=2, color='c')

t2 = np.linspace(np.pi,3*np.pi/2, 100)
x2 = 450 + 100*np.cos(t2)
y2 = 500 - 350*np.sin(t2)
ax.plot(x2, y2, '-', lw=2, color='c')

t3 = np.linspace(np.pi+np.pi/6.5,np.pi/3.1, 100)
x3 = 440 + 100*np.cos(t3)
y3 = 450 - 100*np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color='c')

t5 = np.linspace(4.9*np.pi/6,np.pi/6, 100)
x5 = 795 + 350*np.cos(t5)
y5 = 565 - 350*np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color='c')

t6 = np.linspace(np.pi,3*np.pi/2, 100)
x6 = 11750 + 60*np.cos(t6)
y6 = 450 - 300*np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color='c')


plt.savefig("orion.png")