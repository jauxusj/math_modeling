import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

t0 = np.linspace(np.pi, 0, 10)
x0 = 2*np.cos(t0)
y0 = 2*np.sin(t0)

x1 = np.linspace(2.1, 4, 0.2)
y1 = np.zeros(len(x1))

x = np.append(x0, x1)
y = np.append(y0, y1)

t2 = np.linspace(np.pi*2, np.pi, 10)
x2 = 6 + 2*np.cos(t2)
y2 = 2*np.sin(t2)


x = np.append(x0, x2)
y = np.append(y0, y2)

splire_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, splire_coords )


plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1], 'g')
plt.axis('equal')
plt.savefig("spline.png")