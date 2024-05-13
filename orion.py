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

x = np.append(x0, x1)
y = np.append(y0, y1)

t2 = np.linspace(3*np.pi/2,np.pi, 100)
x2 = 450 + 100*np.cos(t2)
y2 = 500 - 350*np.sin(t2)
ax.plot(x2, y2, '-', lw=2, color='c')

x = np.append(x, x2)
y = np.append(y, y2)

t3 = np.linspace(np.pi+np.pi/6.5,np.pi/3.1, 100)
x3 = 440 + 100*np.cos(t3)
y3 = 450 - 100*np.sin(t3)
ax.plot(x3, y3, '-', lw=2, color='c')

x = np.append(x, x3)
y = np.append(y, y3)

t5 = np.linspace(4.9*np.pi/6,np.pi/6, 100)
x5 = 795 + 350*np.cos(t5)
y5 = 565 - 350*np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color='c')

x = np.append(x, x5)
y = np.append(y, y5)

t6 = np.linspace(np.pi,3*np.pi/2, 100)
x6 = 1200 + 97*np.cos(t6)
y6 = 397 - 300*np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color='c')

x = np.append(x, x6)
y = np.append(y, y6)

t7 = np.linspace(np.pi,3*np.pi/2, 100)
x7 = 1300 + 97*np.cos(t7)
y7 = 700 - 250*np.sin(t7)
ax.plot(x7, y7, '-', lw=2, color='c')

x = np.append(x, x7)
y = np.append(y, y7)

t8 = np.linspace(np.pi,3*np.pi/2, 100)
x8 = 1400 + 97*np.cos(t8)
y8 = 950 - 105*np.sin(t8)
ax.plot(x8, y8, '-', lw=2, color='c')

x = np.append(x, x8)
y = np.append(y, y8)

t9 = np.linspace(-np.pi/6,-2*np.pi/3, 100)
x9 = 1050 + 400*np.cos(t9)
y9 = 895 - 350*np.sin(t9)
ax.plot(x9, y9, '-', lw=2, color='c')

x = np.append(x, x9)
y = np.append(y, y9)

t10 = np.linspace(2*np.pi,3*np.pi/2, 100)
x10 = 710 + 130*np.cos(t10)
y10 = 1200 - 130*np.sin(t10)
ax.plot(x10, y10, '-', lw=2, color='c')

x = np.append(x, x10)
y = np.append(y, y10)

t11 = np.linspace(0,np.pi/5, 100)
x11 = 0 + 700*np.cos(t11)
y11 = 1330 - 530*np.sin(t11)
ax.plot(x11, y11, '-', lw=2, color='c')

x = np.append(x, x11)
y = np.append(y, y11)

t12 = np.linspace(2*np.pi-np.pi/12,12*np.pi/10, 100)
x12 = 455 + 110*np.cos(t12)
y12 = 1000 - 100*np.sin(t12)
ax.plot(x12, y12, '-', lw=2, color='c')

x = np.append(x, x12)
y = np.append(y, y12)

t13 = np.linspace(2*np.pi-np.pi/10,3*np.pi/2, 100)
x13 = 275 + 85*np.cos(t13)
y13 = 1025 - 100*np.sin(t13)
ax.plot(x13, y13, '-', lw=2, color='c')

x = np.append(x, x13)
y = np.append(y, y13)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0) 
figure_spline_part_manual = np.arange(0, 0.5, 0.01) 
spline_curve = interpolate.splev(figure_spline_part, spline_coords) 
 
curve_coords = [] 
for i in range(len(spline_curve[0])): 
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]]) 
 
polygon = geom.Polygon(curve_coords) 
points_number_per_side = 100 
x_pictures_limits = [0, 2000] 
y_pictures_limits = [1400, 0] 
 
for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side): 
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side): 
        p = geom.Point(x_point_coord, y_point_coord) 
        if p.within(polygon): 
            plt.plot(x_point_coord, y_point_coord, 'co', ms = 0.5) 



plt.plot(spline_curve[0], spline_curve[1], 'c', lw=4)
plt.savefig("orion.png")