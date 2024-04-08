from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def circle_move(alpha, vx0, vy0, time):
   t = np.arange(0, 4*np.pi, 0.1)
   x = 12*np.cos(t) + 8*np.cos(1.5*t)
   y = 12*np.sin(t) - 8*np.sin(1.5*t)

   x0 = (vx0 * time) + ((10*time**2)/2) 
   y0 = (vy0 * time) + ((10*time**2)/2) 
   
   X = 5*x*np.cos(alpha) - y*np.sin(alpha) + 10*x0
   Y = 5*y*np.cos(alpha) + x*np.sin(alpha) + 7*y0

   return X, Y              

def animate(alpha):
    ball.set_data(circle_move(alpha=alpha, vx0=-5, vy0=-5, time=alpha))


if __name__ == '__main__':

    fig, ax = plt.subplots()
    ball, = plt.plot([], [], '-', color='y', label='Ball')

    edge = 400
    plt.axis('equal')
    ax.set_ylim(-edge+100, edge)
    ax.set_xlim(-edge+100, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(-4, 2*np.pi, 0.01),
                        interval=30)
    

    ani.save('animation_project.gif')