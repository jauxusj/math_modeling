import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('n.jpg.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

x = [120, 205]
y = [0, 500]

ax.plot(x, y, '-', lw=2, color='w')

plt.savefig("horseapp.png")
