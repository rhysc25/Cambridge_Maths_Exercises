import numpy as np
import matplotlib.pyplot as plt

omega_n = 100
zeta = 0.03
omega_d = omega_n * np.sqrt(1- zeta**2)

t = np.arange(0,0.4,0.003)

y = (omega_n * np.exp(-zeta * omega_n * t) * np.sin(omega_d * t))/(np.sqrt(1-zeta**2))

plt.plot(t,y)
plt.show()
