import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

def selective_filtering(image, threshold):
    # Menerapkan filter Gaussian untuk menghaluskan citra
    smoothed_image = ndimage.gaussian_filter(image, sigma=2)
    # Menghitung citra highpass dengan mengurangi citra asli dengan citra yang telah difilter dengan Gaussian
    highpass_image = image - smoothed_image
    # Menghitung citra frekuensi rendah dan tinggi dengan menggunakan filter threshold
    low_freq = smoothed_image * (smoothed_image < threshold)
    high_freq = highpass_image * (smoothed_image >= threshold)
    # Mengambil citra hasil filter dengan menggabungkan citra frekuensi rendah dan tinggi
    filtered_image = low_freq + high_freq
    filtered_image = filtered_image / filtered_image.max()
    return filtered_image
img = plt.imread('Filter.jpg')
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')
# Menerapkan selective filtering dengan threshold 0.1
threshold = 0.1
filtered_img = selective_filtering(img, threshold)
# Menampilkan citra hasil filter
plt.figure(figsize=(5, 5))
plt.imshow(filtered_img, cmap='gray')
plt.title('Citra Hasil Filter')
plt.axis('off')
plt.show()
