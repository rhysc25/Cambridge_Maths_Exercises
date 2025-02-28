import numpy as np

def one_sided_diff(func, x, h):
    return (func(x+h) - func(x))/h

def two_sided_diff(func, x, h):
    return (func(x+h) - func(x-h))/(2*h)

range = [10**(-n) for n in range(1,5)]

def run():
    print("One Sided Difference:")
    for n in range:
        print(one_sided_diff(np.sin, 0.3, n))

    print("Two Sided Difference:")
    for n in range:
        print(two_sided_diff(np.sin, 0.3, n))