import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('H.jpg')
fig, ax = plt.subplots()
ax.imshow(img)

t0 = np.linspace(np.pi,np.pi/1.9, 100)
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

t4 = np.linspace(3*np.pi/2,2*np.pi,  100)
x4 = 365 + 100*np.cos(t4)
y4 = 175 - 100*np.sin(t4)
ax.plot(x4, y4, '-', lw=2, color='w')

x = np.append(x, x4)
y = np.append(y, y4)

t5 = np.linspace(np.pi, 0 , 100)
x5 = 485 + 20*np.cos(t5)
y5 = 175.5 - 20*np.sin(t5)
ax.plot(x5, y5, '-', lw=2, color='w')

x = np.append(x, x5)
y = np.append(y, y5)

t6 = np.linspace(np.pi, 3*np.pi/2, 100)
x6 = 634.5 + 120*np.cos(t6)
y6 = 174.5 - 20*np.sin(t6)
ax.plot(x6, y6, '-', lw=2, color='w')

x = np.append(x, x6)
y = np.append(y, y6)

t8 = np.linspace( np.pi/2, -np.pi/2+np.pi/9,100)
x8 = 630.5 + 100*np.cos(t8)
y8 = 395.5 - 200*np.sin(t8)
ax.plot(x8, y8, '-', lw=2, color='w')

x = np.append(x, x8)
y = np.append(y, y8)

t9 = np.linspace(np.pi/2+np.pi/12, np.pi+np.pi/12, 100)
x9 = 670 + 35*np.cos(t9)
y9 = 700 - 120*np.sin(t9)
ax.plot(x9, y9, '-', lw=2, color='w')

x = np.append(x, x9)
y = np.append(y, y9)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0) 
figure_spline_part_manual = np.arange(0, 0.5, 0.01) 
spline_curve = interpolate.splev(figure_spline_part, spline_coords) 
 
curve_coords = [] 
for i in range(len(spline_curve[0])): 
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]]) 
 
polygon = geom.Polygon(curve_coords) 
points_number_per_side = 500 
x_pictures_limits = [-100, 900] 
y_pictures_limits = [700, -100] 
points_coords = []

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
    return scalar_func

intensity_centerums_x = [530, 500, 450, 400, 350, 400, 450, 295, 600, 620, 650, 700, 490, 250, 570, 680, 600]
intensity_centerums_y = [400, 500, 600, 600, 625, 685, 300, 650, 350, 300, 230, 400, 450, 680, 680, 580, 450]
intensity_values = [0.1, 0.1, 0.1, 0.01, 0.1, 0.03, 0.09, 0.06, 0.1, 0.06, 0.12, 0.1, 0.05, 0.1, 0.03, 0.02, 0.0]

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0.0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x-int_cen_x[i], y-int_cen_y[i], 0.030, [0.00015, 0.00015])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centerums_x, 
                                intensity_centerums_y, intensity_values)
    scalar_fields.append(calculate)

fig, ax = plt.subplots()
sc_plot = ax.scatter(x_p, y_p, c=scalar_fields)
ax.set_ylabel('Координата Y, м')
ax.set_xlabel('Координата X, м')
plt.ylim(700, 0)

cbar = fig.colorbar(sc_plot)
cbar.set_label("Комбинированное скалярное поле")
plt.savefig("horseapp.png")