import matplotlib.pyplot as plt
import numpy as np
import requests
from io import BytesIO
from PIL import Image

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


import matplotlib.pyplot as plt
import numpy as np
import urllib.request
from PIL import Image

# Define the image URL
url = "http://www-g.eng.cam.ac.uk/125/1950-1975/images/southwing.jpg"

# Open the URL and read the image
with urllib.request.urlopen(url) as response:
    img = Image.open(response)  # Open image using PIL

# Convert the image to a NumPy array
A = np.array(img)

print(A[100][100])
print(type(A[100][100]))

# Display the image
plt.imshow(A, cmap='gray')
plt.axis('off')  # Hide axis
plt.show()

# Print image details
print("Image array shape (pixels): {}".format(A.shape))
print(type(A))

G = np.array([[-1,-1,-1], [-1, 8,-1,], [-1,-1,-1,]]) 
print(G)

B = np.zeros(A.shape)

for i in range(1, B.shape[0]- 1): 
    for j in range(1, B.shape[1]- 1): 
        for k in range(3): 
            for l in range(3): 
                B[i, j] += G[k, l]*A[i- 1 + k, j- 1 + l]

plt.imshow(B, cmap='gray');

C = np.zeros(A.shape, dtype=A.dtype)

for i in range(1, A.shape[0] - 1):
    for j in range(1, A.shape[1] - 1):
        for k in range(3):  # Iterate over R, G, B channels
            a = np.add(A[i+1, j, k], A[i-1, j, k])
            b = np.add(A[i, j-1, k], A[i, j+1, k])
            C[i, j, k] = np.add(a, b) / 4

plt.imshow(C, cmap='gray');