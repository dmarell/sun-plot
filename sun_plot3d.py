import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

mpl.rcParams["figure.dpi"] = 600

df = pd.read_csv(r'sun_power.csv', parse_dates=['sampled'])
df['date'] = df['sampled'].dt.date

fig = plt.figure() #figsize=(6, 4), dpi=300)
ax = fig.gca(projection='3d')

# X: (24,) hour of day (0..23) or minute of day (0..24*60)
# Y: (365,) date, day of year
# Z: (24,365) solar_kw
X = np.arange(0, 24, 1)  # (24,))
Y = np.arange(0, 365, 1)  # (365,))
X, Y = np.meshgrid(X, Y)

data = df.groupby([df['date'], df['sampled'].dt.hour])['solar_kw'].mean()
zeroLine = np.zeros(24)  # 24 assumes "hour" above

# Generate solar_kw lines in Z-layer
Z = np.zeros(X.shape)
i = 0
for row_date in reversed(df.date.unique()):
    zs = pd.Series(zeroLine)  # data is sparse, fill with zeroes
    line_data = data[row_date].combine(zs, max, fill_value=0)
    Z[i] = line_data
    i += 1

ax.auto_scale_xyz([0, 24], [0, 1000], [0, 1])
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis,
                       linewidth=0, antialiased=False)
ax.set_xlim(0, 24)
ax.set_ylim(0, 365)
ax.set_zlim(0, 15)
# Customize the z axis
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.draw()
# plt.savefig('sun_plot3d.svg', dpi=600)
plt.savefig('sun_plot3d.png', dpi=600)
plt.show()
