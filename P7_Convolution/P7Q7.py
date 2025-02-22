import numpy as np
import matplotlib.pyplot as plt

"""The Step Response"""
# Initlise the array for t
t = np.arange(-1.0, 3.0, 0.01)

# Initilise zero array for the step response
h = np.zeros(len(t))

# Generate the step response
for i in range(0, len(t)):
    if t[i] >= 0:
        h[i] = 1 - (8.0/5.0)*np.exp(-1.5*t[i]) + (3.0/5.0)*np.exp(-4*t[i])

# Plot the step response
plt.plot(t, h)
plt.xlabel('t')
plt.ylabel('Step response h(t)');

plt.show()


"""The Impulse Response"""
# Initilise zero array for the impulse response
g = np.zeros(len(t))

# Generate the impulse response
for i in range(0, len(t)):
    if t[i] >= 0:
        g[i] = (12.0/5.0)*np.exp(-1.5*t[i]) - (12.0/5.0)*np.exp(-4*t[i])

# Plot the impulse response
plt.plot(t, g)
plt.xlabel('t')
plt.ylabel('Impulse response g(t)');

plt.show()


"""Input Data"""
# Read in data file from URL
import urllib.request
url = "https://raw.github.com/CambridgeEngineering/Part-IA-ExamplesPapers-Python/master/paper4/f.dat"
response = urllib.request.urlopen(url)
f_data = np.loadtxt(response, dtype=float)

# Plot the data
plt.plot(f_data)
plt.ylabel("Input data");

plt.show()

"""Impulse Response for the Data"""
# Generate the impulse response for the data
# FOR STUDENTS: Try changing the range of t_data
t_data = np.arange(0.0, 5.0, 0.05)
g_data = (12.0/5.0)*(np.exp(-1.5*t_data) - np.exp(-4*t_data))

# Plot the impulse response
plt.plot(t_data, g_data)
plt.xlabel('t')
plt.ylabel('Impulse resposne g(t)');

plt.show()


"""Convolve impulse response and f(t)"""
# Now work out the output by convolving f_data with the impulse response g_data
y_data = 0.05*np.convolve(f_data, g_data)
# Compare the entire input f_data and the output y_data
plt.plot(y_data, 'r', lw=2.0, label='Output y(t)')
plt.plot(f_data, 'b', ls='--', alpha=0.55, label='Input f(t)')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5));

plt.show()