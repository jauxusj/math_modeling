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

t3 = np.linspace(3*np.pi/2+np.pi/4, np.pi/2, 100)
x3 = 366 + 45*np.cos(t3)
y3 = 334 - 60*np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color='w')

x = np.append(x, x3)
y = np.append(y, y3)

t4 = np.linspace(2*np.pi,3*np.pi/2,  100)
x4 = 365 + 100*np.cos(t4)
y4 = 175 - 100*np.sin(t4)
ax.plot(x4, y4, '-', lw=2, color='w')

# x = np.append(x, x4)
# y = np.append(y, y4)

t5 = np.linspace( np.pi,np.pi/2, 100)
x5 = 485 + 20*np.cos(t5)
y5 = 175 - 20*np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color='w')

# x = np.append(x, x5)
# y = np.append(y, y5)

t6 = np.linspace(3*np.pi/2, np.pi,  100)
x6 = 634 + 120*np.cos(t6)
y6 = 174 - 20*np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color='w')

# x = np.append(x, x6)
# y = np.append(y, y6)

t7 = np.linspace(np.pi/10, np.pi/2, 100)
x7 = 485 + 30*np.cos(t7)
y7 = 175 - 20*np.sin(t7)
ax.plot(x7, y7, '-', lw=2, color='w')

# x = np.append(x, x7)
# y = np.append(y, y7)

t8 = np.linspace(np.pi/2, -np.pi/2+np.pi/9, 100)
x8 = 630 + 100*np.cos(t8)
y8 = 395 - 200*np.sin(t8)
ax.plot(x8, y8, '-', lw=2, color='w')

# x = np.append(x, x8)
# y = np.append(y, y8)

t9 = np.linspace(np.pi/2+np.pi/12, np.pi, 100)
x9 = 670 + 35*np.cos(t9)
y9 = 700 - 120*np.sin(t9)
ax.plot(x9, y9, '-', lw=2, color='w')

# x = np.append(x, x9)
# y = np.append(y, y9)


splire_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
figure_spline_part_manual = np.arange(0, 0.5, 0.01)
spline_curve = interpolate.splev(figure_spline_part, splire_coords )

plt.plot(spline_curve[0], spline_curve[1], 'c', lw=4)

plt.savefig("horseapp.png")