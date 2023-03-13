import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
img = cv2.imread('Filter.jpg', 0)

# Compute the DFT of the image
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Compute the magnitude spectrum (logarithmic)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Plot the image and its spectrum
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.imshow(img, cmap='gray')
ax1.set_title('Image')
ax2.imshow(magnitude_spectrum, cmap='gray')
ax2.set_title('Magnitude Spectrum')
plt.tight_layout()
plt.show()
