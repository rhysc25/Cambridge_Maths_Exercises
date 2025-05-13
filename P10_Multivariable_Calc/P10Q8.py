import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2,4,0.1)
y = np.arange(-2,4,0.1)

X, Y = np.meshgrid(x,y)

Z = X*Y*(2- X- 2*Y)
plt.contour(X, Y, Z, 20)

plt.show()