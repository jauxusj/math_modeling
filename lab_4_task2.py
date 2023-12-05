import numpy as np

def func(a):
    x = 1
    for i in a:
        x = x * i 
    return x


c = [1, 2, 3, 4, 5]

print(func(c))