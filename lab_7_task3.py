import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def update(t):
    xdata.append(np.sin(t) * (np.e**(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5))
    ydata.append(np.cos(t) * (np.e**(np.cos(t)) - 2*np.cos(4*t) + np.sin(t/12)**5))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 12*np.pi, 0.1),
                    interval=100
                    )

ani.save('animation_task31.gif')





import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def update(t):
    xdata.append(16*np.sin(t)**3)
    ydata.append(13*np.cos(t)-5*np.cos(2*t)-np.cos(4*t))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig,
                    update,
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100
                    )

ani.save('animation_32.gif')