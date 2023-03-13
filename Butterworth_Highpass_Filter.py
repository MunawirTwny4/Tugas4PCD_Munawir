import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='highpass', analog=False)
    return b, a
def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = filtfilt(b, a, data)
    return y
# Membaca citra grayscale
img = plt.imread('Filter.jpg')
# Menampilkan citra asli
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')
data = img.flatten()
# Menerapkan filter Butterworth highpass dengan frekuensi cutoff 0.05 dan orde 5
fs = 1
cutoff = 0.05
order = 5
filtered_data = butter_highpass_filter(data, cutoff, fs, order=order)
# Mengonversi data hasil filter ke dalam citra grayscale 2D
filtered_img = filtered_data.reshape(img.shape)
# Menampilkan citra hasil filter
plt.figure(figsize=(5, 5))
plt.imshow(filtered_img, cmap='gray')
plt.title('Citra Hasil Filter')
plt.axis('off')
plt.show()