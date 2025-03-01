import numpy as np
from IPython.display import Audio
import matplotlib.pyplot as plt
import scipy
import urllib

url = "https://github.com/CambridgeEngineering/PartIA-Computing-Examples-Papers/raw/main/sound/piano1.wav"
Audio(url)

# Fetch sound file
local_filename, headers = urllib.request.urlretrieve(url)

# Read frequency and data array for sound track
fs, x = scipy.io.wavfile.read(local_filename) 

# If we have a stero track (left and right channels), take just the first channel
if len(x.shape) > 1:
    x = x[:, 0]

# Check that it plays
Audio(x, rate=fs)

# Time points (0 to T, with T*fs points)
t = np.linspace(0, len(x)/fs, len(x), endpoint=False)

# Plot signal
plt.plot(t, x)
plt.xlabel('time (s)')
plt.ylabel('signal');

#Decompose by frequency

# Perform a Fourier transform of the signal (signal is real, so we can use the 'real' version)
xf = np.fft.rfft(x)

# Create frequency axis
freq = np.linspace(0.0, fs/2, len(xf))

# Plot Fourier coefficients against frequency. Fourier coefficients are complex, so
# we take the modulus.
plt.plot(freq, np.abs(xf))
plt.xlabel('frequency (Hz)')
plt.ylabel('x');
plt.xlim(0,5000)

# Copy transformed problem
xf_filtered1 = xf.copy()
xf_filtered2 = xf.copy()


# Cut off requencies above 700 Hz


cutoff_freq = 700
n_cut = int(2*cutoff_freq*len(xf_filtered1)/fs)
xf_filtered1[n_cut:] = 0.0

plt.plot(freq, np.abs(xf_filtered1))
plt.xlabel('frequency (Hz)')
plt.ylabel('x')
plt.xlim(0, 800);

# Perform inverse transfiorm
x_filtered = np.fft.irfft(xf_filtered1)

# Plot signal over first 0.05 s
n = int(0.05*fs)
plt.plot(t[:n], x_filtered[:n])
plt.xlabel('time (s)')
plt.ylabel('$x(t)$')

Audio(x_filtered, rate=fs)


# Cut off frequency below 700

n_cut = int(2*cutoff_freq*len(xf_filtered2)/fs)
xf_filtered2[:n_cut] = 0.0

plt.plot(freq, np.abs(xf_filtered2))
plt.xlabel('frequency (Hz)')
plt.ylabel('x')
plt.xlim(500, 10000);

# Perform inverse transfiorm
x_filtered3 = np.fft.irfft(xf_filtered2)

# Plot signal over first 0.05 s
n = int(0.05*fs)
plt.plot(t[:n], x_filtered3[:n])
plt.xlabel('time (s)')
plt.ylabel('$x(t)$')

Audio(x_filtered3, rate=fs)