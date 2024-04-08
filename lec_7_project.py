from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

def star2(vx0, vy0,time, alpha):
   t2 = np.arange(0, 4*np.pi, 0.1)
   x2 = 12*np.cos(t2) + 8*np.cos(1.5*t2)
   y2 = 12*np.sin(t2) - 8*np.sin(1.5*t2)

   x02 = (vx0 * time)
   y02 = (vy0 * time) 
   
   X2 = 10*x2*np.cos(alpha) - y2*np.sin(alpha) + 10*x02
   Y2 = 10*y2*np.cos(alpha) + x2*np.sin(alpha) + 7*y02

   return X2, Y2               


def star3(vx0, vy0,time, alpha):
   t3 = np.arange(0, 4*np.pi, 0.1)
   x3 = 12*np.cos(t3) + 8*np.cos(1.5*t3)
   y3 = 12*np.sin(t3) - 8*np.sin(1.5*t3)

   x02 = -(vx0 * time)
   y02 = -(vy0 * time) 
   
   X3 = 18*x3*np.cos(alpha) - y3*np.sin(alpha) + 7*x02
   Y3 = 18*y3*np.cos(alpha) + x3*np.sin(alpha) + 7*y02

   return X3, Y3               



def circle_move(alpha, vx0, vy0, time):
   t = np.arange(0, 4*np.pi, 0.1)
   x = 12*np.cos(t) + 8*np.cos(1.5*t)
   y = 12*np.sin(t) - 8*np.sin(1.5*t)

   x0 = (vx0 * time) + ((10*time**2)/2) 
   y0 = (vy0 * time) + ((10*time**2)/2) 
   
   X = 6*x*np.cos(alpha) - y*np.sin(alpha) + 10*x0
   Y = 6*y*np.cos(alpha) + x*np.sin(alpha) + 7*y0

   return X, Y      


def circle_move1(alpha, vx04, vy04, time):
   t4 = np.arange(0, 4*np.pi, 0.1)
   x4 = 12*np.cos(t4) + 8*np.cos(1.5*t4)
   y4 = 12*np.sin(t4) - 8*np.sin(1.5*t4)

   x04 = -(vx04 * time) - ((10*time**2)/2) 
   y04 = -(vy04 * time) - ((10*time**2)/2) 
   
   X4 = 3*x4*np.cos(alpha) - y4*np.sin(alpha) + 10*x04
   Y4 = 3*y4*np.cos(alpha) + x4*np.sin(alpha) + 7*y04

   return X4, Y4

def animate(alpha):
    ball.set_data(circle_move(alpha=alpha, vx0=-6, vy0=-6, time=alpha))
    ball2.set_data(circle_move1(alpha=alpha, vx04=-6, vy04=-6, time=alpha))
    star.set_data(star2(alpha=alpha, vx0=-11, vy0=-11, time=alpha))
    star1.set_data(star3(alpha=alpha, vx0=-11, vy0=-11, time=alpha))

if __name__ == '__main__':

    fig, ax = plt.subplots()
    star1, = plt.plot([], [], '-', color='y', label='Star')
    ball, = plt.plot([], [], '-', color='r', label='Ball')
    ball2, = plt.plot([], [], '-', color='m', label='Ballka')
    star, = plt.plot([], [], '-', color='g', label='Starka')

    edge = 400
    plt.axis('equal')
    ax.set_ylim(-edge, edge)
    ax.set_xlim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=np.arange(-4, 2*np.pi, 0.01),
                        interval=30)
    

    ani.save('animation_project.gif')