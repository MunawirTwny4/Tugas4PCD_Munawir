import cv2
import numpy as np

# Load the image
img = cv2.imread('Filter.jpg', 0)

# Fourier Transform
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Filter
rows, cols = img.shape
crow, ccol = rows//2, cols//2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0

# Inverse Fourier Transform
ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(ishift)
img_back = np.abs(img_back)

# Display the result
cv2.imshow('Original Image', img)
cv2.imshow('High Pass Filtered Image', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
