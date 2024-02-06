import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter(k=5):

    x = np.arange(0.01, 20, 0.01)
    y = k/x

    plt.plot(x, y)
    plt.savefig('fig_task2.png')

if __name__ == '__main__':
    giperbola_plotter()