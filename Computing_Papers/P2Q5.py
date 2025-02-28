import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,50)
f = np.sin(x)+(np.cos(10*x)/5)

plt.plot(x,f)

def avrg(h):
    smoothed = np.zeros_like(f)
    smoothed[0] = f[0]
    smoothed[-1] = f[-1]
    for i in range(1,len(f)-1):
        smoothed[i] = (f[i-1]+f[i]+f[i+1])/3
    return smoothed

smoothed = avrg(f)

plt.plot(x,smoothed)
plt.show()






