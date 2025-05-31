import numpy as np
import matplotlib.pyplot as plt

def impulse_response(t):
    
    omega_n = 100
    zeta = 0.03
    omega_d = omega_n * np.sqrt(1- zeta**2)

    g = (omega_n * np.exp(-zeta * omega_n * t) * np.sin(omega_d * t))/(np.sqrt(1-zeta**2))

    plt.plot(t,g)
    plt.show()

    return g

def generic_wave(t):

    freq = 80

    omega = 2 * np.pi * freq
    wave = np.sin(omega * t)

    plt.plot(t,wave)
    plt.show()

    return wave

def convolution(t, g, wave):
    result = np.convolve(wave, g, mode='full')  # or 'same'

    # Generate time axis for the convolution result
    dt = t[1] - t[0]
    t_conv = np.arange(0, len(result)) * dt

    plt.figure()
    plt.plot(t_conv, result)
    plt.title("Convolution Result")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    t = np.arange(0,0.4,0.003)

    g = impulse_response(t)
    wave = generic_wave(t)

    convolution(t,g,wave)
    
