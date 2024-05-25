import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom
import h5py

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
points_number_per_side = 700 
x_pictures_limits = [1400, 0] 
y_pictures_limits = [1400, 0] 

points_coords = []
background_coords = []
for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side): 
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side): 
        p = geom.Point(x_point_coord, y_point_coord) 
        if p.within(polygon): 
             points_coords.append(x_point_coord)
             points_coords.append(y_point_coord)
        else:
            background_coords.append(x_point_coord)
            background_coords.append(y_point_coord)



x_p = np.array(points_coords[0::2]) / 1600
y_p = np.array(points_coords[1::2]) / 1600

x_bg = np.array(background_coords[0::2]) / 1600
y_bg = np.array(background_coords[1::2]) / 1600


########################################################
float_type = np.float64
int_type = np.int32
box_size = 1.2


m_0 = 2*1.6735575e-24 # масса молекулы водорода в граммах
n_0 = 2*10**5 # характерная концентрация частиц в частицах на куб. см

m_unit = 2*10**33 # единица массы (солнечная масса)
len_unit = 9.460e17 # единица длины (1 парсек)
vel_unit = 100 # единица скорости (1 м/с)

len_nebulas_x = 1
len_nebulas_y = 1
square_nebulas = len_nebulas_x * len_nebulas_y / len(x_p)

scale_0 = 0.1 * len_unit # характерная толщина туманности
rho_gass_in_square = m_0 * n_0 * scale_0
gas_mass = rho_gass_in_square * square_nebulas

gas_part_num = len(x_p)
gas_coords = np.zeros([gas_part_num, 3], dtype=float_type)
gas_vel = np.zeros([gas_part_num, 3], dtype=float_type)
gas_masses = np.zeros(gas_part_num, dtype=float_type)

for i in range(len(x_p)):
    gas_coords[i, 0] = x_p[i]
    gas_coords[i, 1] = y_p[i]

    gas_vel[i, 0] = float_type(0.001)
    gas_vel[i, 1] = float_type(0.0)
    
    gas_masses[i] = gas_mass 


##############################################
background_parts = 500

m_bg = 2*1.6735575e-24 # масса молекулы вакуума
n_bg = 2*10**1 # характерная концентрация частиц в вакууме

square_bg = box_size**2 / background_parts

scale_0 = 0.1 * len_unit # характерная толщина туманности
rho_bg_in_square = m_bg * n_bg * scale_0
bg_mass = rho_bg_in_square * square_bg

bg_coords = np.zeros([background_parts, 3], dtype=float_type)
bg_velocity = np.zeros([background_parts, 3], dtype=float_type)
bg_masses =  np.zeros(background_parts, dtype=float_type)

step = int(len(x_bg) / background_parts)

for i in range(background_parts):
    bg_coords[i, 0] = x_bg[i*step]
    bg_coords[i, 1] = y_bg[i*step]

    bg_masses[i] = bg_mass

all_parts = gas_part_num + background_parts
all_coords = np.zeros([all_parts, 3], dtype=float_type)
all_velocity = np.zeros([all_parts, 3], dtype=float_type)

for i in range(all_parts):
    if i < gas_part_num:
        all_coords[i, :] = gas_coords[i, :]
        all_velocity[i, :] = gas_vel[i, :]
    else:
        all_coords[i, :] = bg_coords[i-gas_part_num, :]
        all_velocity[i, :] = bg_velocity[i-gas_part_num, :]

all_mass = np.append(gas_masses, bg_mass)


##############################################
IC = h5py.File('./Orion.hdf5', 'w')
header = IC.create_group("Header") 
part0 = IC.create_group("PartType0")

KEY_STUB = 0
KEY_STUB_ARRAY = np.ones(6, dtype = int_type)
num_part = np.array([all_parts, 0, 0, 0, 0, 0], dtype=int_type)
header.attrs.create("NumPart_ThisFile", num_part)
header.attrs.create("NumPart_Total_HighWord", np.zeros(6, dtype=int_type))
header.attrs.create("NumPart_Total", num_part)
header.attrs.create("MassTable", KEY_STUB_ARRAY)
header.attrs.create("Time", KEY_STUB)
header.attrs.create("BoxSize", box_size)
header.attrs.create("Redshift", KEY_STUB)
header.attrs.create("Omega0", KEY_STUB)
header.attrs.create("OmegaB", KEY_STUB)
header.attrs.create("OmegaLambda", KEY_STUB)
header.attrs.create("HubbleParam", KEY_STUB)
header.attrs.create("Flag_Sfr", KEY_STUB)
header.attrs.create("Flag_Cooling", KEY_STUB)
header.attrs.create("Flag_StellarAge", KEY_STUB)
header.attrs.create("Flag_Metals", KEY_STUB)
header.attrs.create("Flag_Feedback", KEY_STUB)
header.attrs.create("NumFilesPerSnapshot", KEY_STUB)
header.attrs.create("Flag_DoublePrecision", 1)

part0.create_dataset("ParticleIDs", data=np.arange(0, all_parts))
part0.create_dataset("Coordinates", data=all_coords)
part0.create_dataset("Velocities", data=all_velocity)
part0.create_dataset("Masses", data=all_mass)

IC.close()



# def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
#     scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
#     return scalar_func

# intensity_centerums_x = []
# intensity_centerums_y = []
# intensity_values = []

# def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
#     scalar_field = 0.0
#     for i in range(0, len(int_cen_x)):
#         scalar_field += int_vel[i] * bell_function(x-int_cen_x[i], y-int_cen_y[i], 0.0030, [0.000035, 0.000035])
#     return scalar_field

# scalar_fields = []
# for i in range(0, len(x_p)):
#     calculate = scalar_function(x_p[i], y_p[i], intensity_centerums_x, 
#                                 intensity_centerums_y, intensity_values)
#     scalar_fields.append(calculate)

# fig, ax = plt.subplots()
# sc_plot = ax.scatter(x_p, y_p, c=scalar_fields)
# ax.set_ylabel('Координата Y, м')
# ax.set_xlabel('Координата X, м')

# plt.ylim(1400, 0)
# cbar = fig.colorbar(sc_plot)
# cbar.set_label("Комбинированное скалярное поле")
# plt.savefig("orion.png")