import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def createSomeShape(Z):
    Z[10][1] = 6
    Z[10][2] = 7
    Z[10][3] = 8
    Z[10][4] = 9
    Z[10][5] = 10
    Z[10][6] = 11
    Z[10][7] = 12
    Z[10][8] = 13
    Z[10][9] = 14
    Z[10][10] = 15
    Z[10][11] = 16
    Z[10][12] = 16
    Z[10][13] = 16
    Z[10][14] = 14
    Z[10][15] = 12
    Z[10][16] = 10
    Z[10][17] = 8
    Z[10][18] = 6

    Z[11][1] = 6
    Z[11][2] = 7
    Z[11][3] = 8
    Z[11][4] = 9
    Z[11][5] = 10
    Z[11][6] = 11
    Z[11][7] = 12
    Z[11][8] = 13
    Z[11][9] = 14
    Z[11][10] = 15
    Z[11][11] = 16
    Z[11][12] = 16
    Z[11][13] = 16
    Z[11][14] = 14
    Z[11][15] = 12
    Z[11][16] = 10
    Z[11][17] = 8
    Z[11][18] = 6

    Z[12][1] = 6
    Z[12][2] = 7
    Z[12][3] = 8
    Z[12][4] = 9
    Z[12][5] = 10
    Z[12][6] = 11
    Z[12][7] = 12
    Z[12][8] = 13
    Z[12][9] = 14
    Z[12][10] = 15
    Z[12][11] = 16
    Z[12][12] = 16
    Z[12][13] = 16
    Z[12][14] = 14
    Z[12][15] = 12
    Z[12][16] = 10
    Z[12][17] = 8
    Z[12][18] = 6

fig = plt.figure()
ax = fig.gca(projection='3d')

# X: (24,) hour of day (0..23) or minute of day (0..24*60)
# Y: (365,) date, day of year
# Z: (24,365) solar_kw

X = np.arange(0, 24, 1)  # (24,))
Y = np.arange(0, 36, 1)  # (365,))
X, Y = np.meshgrid(X, Y)

Z = np.ones(X.shape) * 5
createSomeShape(Z)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis
ax.set_zlim(0, 20)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
