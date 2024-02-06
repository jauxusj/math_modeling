import matplotlib.pyplot as plt
import numpy as np

def elips_plotter(a=8, b=6):

    x = np.arange(-20, 20, 0.1)
    y = np.arange(-20, 20, 0.1)

    X, Y = np.meshgrid(x, y)

    fxy = X**2/a**2 + Y**2/b**2

    plt.contour(X, Y, fxy, levels=[1])
    plt.axis('equal')

    plt.savefig('fig_task3.png')

if __name__ == '__main__':
    elips_plotter()