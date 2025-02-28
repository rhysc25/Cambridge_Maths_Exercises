import numpy as np


axis = np.arange(0, 2*np.pi, 0.0001)
sin = np.sin(axis)

# axis[3000] = 0.3
# cos(0.3) = 0.9553364891

def one_sided_diff(func, x, h):
    return (func[x+h] - func[x])/h

def two_sided_diff(func, x, h):
    return (func[x+h] - func[x-h])/(2*h)

range = [10**(-n) for n in range(1,5)]

print("One Sided Difference:")
for n in range:
    print(10000*one_sided_diff(sin, 3000, int(n*10000)))

print("Two Sided Difference:")
for n in range:
    print(10000*two_sided_diff(sin, 3000, int(n*10000)))