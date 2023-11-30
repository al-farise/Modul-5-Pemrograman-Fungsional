import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 8, 5]

# Menambahkan titik baru
x_new = [3, 5, 8, 9, 0]
y_new = [6, 4, 3, 0, 2]

# Menambahkan Judul
plt.title('Titik-titik')
plt.scatter(x, y)
# Menambahkan titik baru
plt.scatter(x_new, y_new)
plt.show()