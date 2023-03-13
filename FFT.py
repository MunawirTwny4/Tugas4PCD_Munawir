import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image and convert it to grayscale
img = cv2.imread('Filter.jpg', 0)

# Compute the FFT of the image
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Compute the magnitude spectrum of the FFT
magnitude_spectrum = 20*np.log(np.abs(fshift))

# Plot the original image and its spectrum
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(img, cmap='gray')
ax1.set_title('Input Image')
ax1.set_xticks([])
ax1.set_yticks([])
ax2.imshow(magnitude_spectrum, cmap='gray')
ax2.set_title('Magnitude Spectrum')
ax2.set_xticks([])
ax2.set_yticks([])
plt.show()
