import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-4*np.pi, 4*np.pi, 0.01)

h = np.zeros(len(t))

N = 6

for i in range(0, len(t)):
    h[i] = 0.5
    for n in range(1,N):
        h[i] += ((np.sin(n*np.pi)/(n*np.pi))*np.cos(n*t[i]) + ((1-np.cos(n*np.pi))/(n*np.pi))*np.sin(n*t[i]))
        

plt.plot(t,h)
plt.show()