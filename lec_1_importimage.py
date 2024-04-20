import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('n.jpg')
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, 1000, 0, 200])
plt.ylim(0, 600)
plt.savefig("horse.png")