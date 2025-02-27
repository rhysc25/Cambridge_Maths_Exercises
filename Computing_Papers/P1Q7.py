import matplotlib.pyplot as plt
import numpy as np

#Parameters
m = 1
k = 40
f = 0
dt = 0.01
x_0,x_1=0.01,0.01

times = [i*dt for i in range(2001)]

anal_sol = [((0.01-(f/k))*np.cos(times[i]*np.sqrt(k/m))+(f/k)) for i in range(len(times))]

#For f=0
#num_sol = np.zeros(2001)
#num_sol[0],num_sol[1]=x_0,x_1
#for i in range(2,len(num_sol)):
#  num_sol[i] = (2-((dt**2 * k)/m))*num_sol[i-1] - num_sol[i-2] + (dt**2 * f)/m

#For f=0.025
num_sol = np.zeros(2001)
num_sol[0],num_sol[1]=x_0,x_1
for i in range(2,len(num_sol)):
  f=-0.025 if num_sol[i-1]>num_sol[i-2] else 0.025
  num_sol[i] = (2-((dt**2 * k)/m))*num_sol[i-1] - num_sol[i-2] + (dt**2 * f)/m

plt.plot(times,num_sol, label="Numerical")
plt.plot(times,anal_sol, label="Analytical")
plt.legend()
plt.show()