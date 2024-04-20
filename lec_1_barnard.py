import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('Barnard_68.jpg')

fig, ax = plt.subplots()
ax.imshow(img)

t = np.linspace(np.pi/2, 3*np.pi/2, 100 )
x = 180 + 40*np.cos(t)
y = 430 + 40*np.sin(t)
ax.plot(x, y, '-', lw=2, color='m')

t = np.linspace(3*np.pi/2, 2*np.pi, 100 )
x = 200 + 40*np.cos(t)
y = 400 + 40*np.sin(t)
ax.plot(x, y, '-', lw=2, color='m')


plt.savefig("barnard.png")