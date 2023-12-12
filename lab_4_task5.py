import numpy as np

def func(figure, r=0, a=0, h=0):
    ''' figure - 1 = circle, figure - 2 = square, figure - 3 = rectangle
    '''
    if figure == 1:
        S = np.pi * r**2
    elif figure == 2:
        S = a**2
    else:
        S = a * h/2

    return S

print(func(2, a=3))