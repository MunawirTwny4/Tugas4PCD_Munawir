import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def unsharp_masking_filter(image, sigma, amount):
    # Menerapkan filter Gaussian
    smoothed_image = ndimage.gaussian_filter(image, sigma=sigma)
    # Menghitung citra highpass dengan mengurangi citra asli dengan citra yang telah difilter dengan Gaussian
    highpass_image = image - smoothed_image
    # Menghitung citra sharpened dengan menambahkan citra highpass yang telah dikalikan dengan faktor amount pada citra asli
    sharpened_image = image + amount * highpass_image
    # Menormalisasi citra hasil sharpening
    sharpened_image = sharpened_image / sharpened_image.max()
    return sharpened_image
# Membaca citra grayscale
img = plt.imread('Filter.jpg')
# Menampilkan citra asli
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

# Menerapkan filter unsharp masking dengan sigma 1.5 dan amount 0.5
sigma = 1.5
amount = 0.5
filtered_img = unsharp_masking_filter(img, sigma, amount)
# Menampilkan citra hasil filter
plt.figure(figsize=(5, 5))
plt.imshow(filtered_img, cmap='gray')
plt.title('Citra Hasil Filter')
plt.axis('off')
plt.show()
