import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('H.jpg')

fig, ax = plt.subplots()
ax.imshow(img)

t = np.linspace(np.pi-np.pi/6.5,np.pi/1.9, 100)
x = 390 + 240*np.cos(t)
y = 800 - 220*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(3*np.pi/2, 2*np.pi, 100)
x = 375 + 100*np.cos(t)
y = 350 - 230*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

x = [475, 395]
y = [350, 376]
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/2, 3*np.pi/2+np.pi/4, 100)
x = 366 + 45*np.cos(t)
y = 334 - 60*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(3*np.pi/2, 2*np.pi, 100)
x = 365 + 100*np.cos(t)
y = 175 - 100*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/2, np.pi, 100)
x = 485 + 20*np.cos(t)
y = 175 - 20*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi, 3*np.pi/2, 100)
x = 634 + 120*np.cos(t)
y = 174 - 20*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/10, np.pi/2, 100)
x = 485 + 30*np.cos(t)
y = 175 - 20*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(-np.pi/2+np.pi/9, np.pi/2, 100)
x = 630 + 100*np.cos(t)
y = 395 - 200*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

t = np.linspace(np.pi/2+np.pi/12, np.pi, 100)
x = 670 + 35*np.cos(t)
y = 700 - 120*np.sin(t)
ax.plot(x, y, '-', lw=2, color='w')

plt.savefig("horseapp.png")