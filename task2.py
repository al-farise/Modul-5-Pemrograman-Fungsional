import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

# Mengubah ukuran figure
plt.figure(figsize=(10,7))
# Menambahkan Judul
plt.title('Sebuah Grafik')
# Mengubah warna garis
plt.plot(xpoints, ypoints, color='orange')
plt.xlim([0,15])
plt.ylim([0,15])
plt.show()