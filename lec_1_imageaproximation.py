import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('H.jpg')

fig, ax = plt.subplots()
ax.imshow(img)

t = np.linspace(np.pi-np.pi/6,np.pi/1.9, 100)
x = 390 + 240*np.cos(t)
y = 800 - 220*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(3*np.pi/2, 2*np.pi, 100)
x = 375 + 100*np.cos(t)
y = 350 - 230*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

x = [475, 395]
y = [350, 375]
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/2, 3*np.pi/2+np.pi/4, 100)
x = 366 + 40*np.cos(t)
y = 334 - 60*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

plt.savefig("horseapp.png")