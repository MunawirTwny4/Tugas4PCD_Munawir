import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def gaussian_highpass_filter(image, sigma):
    # Menerapkan filter Gaussian
    smoothed_image = ndimage.gaussian_filter(image, sigma=sigma)

    # Menghitung citra highpass dengan mengurangi citra asli dengan citra yang telah difilter dengan Gaussian
    highpass_image = image - smoothed_image

    # Menormalisasi citra hasil highpass
    highpass_image = highpass_image / highpass_image.max()
    return highpass_image
# Membaca citra grayscale
img = plt.imread('Filter.jpg')
# Menampilkan citra asli
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

# Menerapkan filter Gaussian highpass dengan sigma 1.5
sigma = 1.5
filtered_img = gaussian_highpass_filter(img, sigma)

# Menampilkan citra hasil filter
plt.figure(figsize=(5, 5))
plt.imshow(filtered_img, cmap='gray')
plt.title('Citra Hasil Filter')
plt.axis('off')
plt.show()
