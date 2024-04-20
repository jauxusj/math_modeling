import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

img = plt.imread('H.jpg')

fig, ax = plt.subplots()
ax.imshow(img)

t0 = np.linspace(np.pi-np.pi/6.5,np.pi/1.9, 100)
x0 = 390 + 240*np.cos(t0)
y0 = 800 - 220*np.sin(t0)
ax.plot(x0, y0, '-', lw=2, color='w')

t1 = np.linspace(3*np.pi/2, 2*np.pi, 100)
x1 = 375 + 100*np.cos(t1)
y1 = 350 - 230*np.sin(t1)
ax.plot(x1, y1, '-', lw=2, color='w')

x = np.append(x0, x1)
y = np.append(y0, y1)

x2 = [475, 395]
y2 = [350, 376]
ax.plot(x2, y2, '-', lw=2, color='w')

x = np.append(x, x2)
y = np.append(y, y2)

t3 = np.linspace(np.pi/2, 3*np.pi/2+np.pi/4, 100)
x3 = 366 + 45*np.cos(t3)
y3 = 334 - 60*np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color='w')

x = np.append(x, x3)
y = np.append(y, y3)

# t = np.linspace(3*np.pi/2, 2*np.pi, 100)
# x = 365 + 100*np.cos(t)
# y = 175 - 100*np.sin(t)
# ax.plot(x, y, '-', lw=2, color='w')

# t = np.linspace(np.pi/2, np.pi, 100)
# x = 485 + 20*np.cos(t)
# y = 175 - 20*np.sin(t)
# ax.plot(x, y, '-', lw=2, color='w')

# t = np.linspace(np.pi, 3*np.pi/2, 100)
# x = 634 + 120*np.cos(t)
# y = 174 - 20*np.sin(t)
# ax.plot(x, y, '-', lw=2, color='w')

# t = np.linspace(np.pi/10, np.pi/2, 100)
# x = 485 + 30*np.cos(t)
# y = 175 - 20*np.sin(t)
# ax.plot(x, y, '-', lw=2, color='w')

# t = np.linspace(-np.pi/2+np.pi/9, np.pi/2, 100)
# x = 630 + 100*np.cos(t)
# y = 395 - 200*np.sin(t)
# ax.plot(x, y, '-', lw=2, color='w')

# t = np.linspace(np.pi/2+np.pi/12, np.pi, 100)
# x = 670 + 35*np.cos(t)
# y = 700 - 120*np.sin(t)
# ax.plot(x, y, '-', lw=2, color='w')


splire_coords, figure_spline_part = interpolate.splprep([x, y], s=0)

spline_curve = interpolate.splev(figure_spline_part, splire_coords )
plt.plot(spline_curve[0], spline_curve[1], 'g', lw=4)

plt.savefig("horseapp.png")